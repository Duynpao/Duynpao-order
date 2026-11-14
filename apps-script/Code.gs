// Nhận đơn từ trang đặt hàng DUYNPAO và ghi vào tab "Đơn hàng" của file "Đơn sỉ Duynpao".
// Ghi theo đúng định dạng đơn lẻ đang dùng: mã LE..., mỗi loại bánh một dòng tính theo bánh,
// phí giao là một dòng riêng, trạng thái "Chờ xác nhận".
// Chỉ ghi cột A:P. Cột Q để trống, cột R:S là công thức của Sheet nên không đụng tới.

const SHEET_ID = '1zwbhIyKhNFw5Le41XbUJ_IFdeZWBq-yPTNOSN8tsZl4';
const TAB = 'Đơn hàng';
const TZ = 'Asia/Ho_Chi_Minh';

// Mã trên trang web -> tên bánh trong file sỉ, giá bán lẻ theo hộp/túi, số bánh mỗi hộp/túi.
// unit = 'bánh': quy ra số bánh, đơn giá = giá hộp / số bánh.
// unit khác: giữ nguyên theo hộp/túi như các đơn lẻ cũ.
const CATALOG = {
  SP001: { name: 'Thịt 1 trứng',       price: 48000,  per: 4,  unit: 'bánh' },
  SP002: { name: 'Đậu dừa',            price: 40000,  per: 4,  unit: 'bánh' },
  SP003: { name: 'Xúc xích phomai',    price: 60000,  per: 4,  unit: 'bánh' },
  SP004: { name: 'Cốm dừa',            price: 60000,  per: 4,  unit: 'bánh' },
  SP005: { name: 'Gà nấm phomai',      price: 60000,  per: 4,  unit: 'bánh' },
  SP006: { name: 'Bò ngô phomai',      price: 60000,  per: 4,  unit: 'bánh' },
  SP007: { name: 'Xá xíu phomai',      price: 60000,  per: 4,  unit: 'bánh' },
  SP008: { name: 'Chay sữa',           price: 25000,  per: 5,  unit: 'bánh' },
  SP009: { name: 'Gạo lứt',            price: 35000,  per: 5,  unit: 'bánh' },
  SP010: { name: 'Nguyên cám',         price: 35000,  per: 5,  unit: 'bánh' },
  SP011: { name: 'Chay sữa túi 500gr', price: 40000,  per: 0,  unit: 'túi 500gr' },
  SP012: { name: 'Cốm mini',           price: 100000, per: 10, unit: 'hộp 10 bánh' },
  SP013: { name: 'Thịt hành mini',     price: 60000,  per: 10, unit: 'hộp 10 bánh' },
  SP014: { name: 'Kimsa trứng muối',   price: 100000, per: 10, unit: 'hộp 10 bánh' },
  SP015: { name: 'Thịt 2 trứng',       price: 60000,  per: 4,  unit: 'bánh' },
};

const SHIP_NEAR = 15000;      // dưới 3km
const SHIP_FAR = 20000;       // trên 3km
const FREE_SHIP_FROM = 200000; // miễn ship khi đơn từ mức này và dưới 3km

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const d = JSON.parse(e.postData.contents);
    const phone = String(d.phone || '').replace(/[^\d+]/g, '');
    if (!/^\+?\d{9,12}$/.test(phone)) return out({ ok: false, error: 'SĐT không hợp lệ' });

    const items = (d.items || [])
      .filter(function (it) { return CATALOG[it.id] && Number(it.qty) > 0 && Number(it.qty) <= 200; })
      .slice(0, 20);
    if (!items.length) return out({ ok: false, error: 'Chưa chọn bánh' });

    const now = new Date();
    const today = Utilities.parseDate(Utilities.formatDate(now, TZ, 'yyyy-MM-dd'), TZ, 'yyyy-MM-dd');
    const orderId = 'LE' + Utilities.formatDate(now, TZ, 'yyMMdd') + '-' +
      String(Math.floor(10000 + Math.random() * 90000));
    const month = Utilities.formatDate(now, TZ, 'yyyy-MM');
    const delivery = d.mode === 'delivery';
    const packing = delivery ? 'Khách lẻ · Giao tận nơi' : 'Khách lẻ · Qua xưởng lấy';
    const name = clip(d.name, 60) || 'Khách web';
    const place = clip(d.place, 200);
    const address = delivery ? place : (place ? 'Lấy tại: ' + place : '');
    const note = ['Web', clip(d.note, 200)].filter(String).join(' · ');

    const rows = [];
    let subtotal = 0;
    items.forEach(function (it) {
      const p = CATALOG[it.id];
      const boxes = Math.floor(Number(it.qty));
      let qty, unitPrice, buns;
      if (p.unit === 'bánh') {
        qty = boxes * p.per;
        unitPrice = p.price / p.per;
        buns = qty;
      } else {
        qty = boxes;
        unitPrice = p.price;
        buns = boxes * p.per;
      }
      const amount = qty * unitPrice;
      subtotal += amount;
      rows.push([now, month, orderId, name, phone, address, today, packing,
        p.name, qty, p.unit, unitPrice, amount, buns, note, 'Chờ xác nhận']);
    });

    if (delivery) {
      const far = String(d.distance) === '1';
      const ship = (!far && subtotal >= FREE_SHIP_FROM) ? 0 : (far ? SHIP_FAR : SHIP_NEAR);
      rows.push([now, month, orderId, name, phone, address, today, packing,
        far ? 'Phí giao (trên 3 km)' : 'Phí giao (dưới 3 km)', 1, 'lần', ship, ship, 0, note, 'Chờ xác nhận']);
    }

    const sh = SpreadsheetApp.openById(SHEET_ID).getSheetByName(TAB);
    // Dòng trống đầu tiên theo cột A (cột R:S có công thức kéo dài nên không dùng getLastRow).
    const colA = sh.getRange('A2:A').getValues();
    let start = 2;
    while (start - 2 < colA.length && colA[start - 2][0] !== '') start++;
    const need = start + rows.length - 1 - sh.getMaxRows();
    if (need > 0) sh.insertRowsAfter(sh.getMaxRows(), need);

    // Tab "Đơn hàng" là một Bảng (Table) đã định kiểu sẵn từng cột, nên không đổi định dạng ô.
    // Thêm dấu ' trước tháng và SĐT để Sheets giữ dạng chữ (không mất số 0 đầu).
    rows.forEach(function (r) { r[1] = "'" + r[1]; r[4] = "'" + r[4]; });
    sh.getRange(start, 1, rows.length, 16).setValues(rows);

    return out({ ok: true, orderId: orderId });
  } catch (err) {
    return out({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

function doGet() {
  return out({ ok: true, msg: 'DUYNPAO nhận đơn web đang chạy' });
}

function clip(s, n) {
  return String(s || '').trim().slice(0, n);
}

function out(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
