// Nhận đơn từ trang đặt hàng DUYNPAO và ghi vào tab "Đơn hàng".
// Mỗi loại bánh ghi một dòng. Tên bánh, đơn giá, thành tiền do công thức trong Sheet tự tính.

const SHEET_ID = '1PVzTmJndt1Orvom-msTikVs9vvSx8CRBDNEosaRAr-Y';
const TAB = 'Đơn hàng';

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const d = JSON.parse(e.postData.contents);
    if (!d.items || !d.items.length || !d.phone) {
      return out({ ok: false, error: 'Thiếu bánh hoặc SĐT' });
    }
    const sh = SpreadsheetApp.openById(SHEET_ID).getSheetByName(TAB);

    // Tìm dòng trống đầu tiên theo cột A (không dùng getLastRow vì cột công thức kéo dài).
    const colA = sh.getRange('A2:A').getValues();
    let row = 2;
    while (row - 2 < colA.length && colA[row - 2][0] !== '') row++;

    const now = new Date();
    const orderId = 'DH' + Utilities.formatDate(now, 'Asia/Ho_Chi_Minh', 'yyMMdd-HHmmss');
    const mode = d.mode === 'delivery' ? 'Giao tận nơi' : 'Tự lấy';
    const note = [orderId, d.note || ''].filter(String).join(' · ');

    d.items.forEach(function (it, i) {
      const r = row + i;
      sh.getRange(r, 1, 1, 3).setValues([[now, String(d.phone), String(it.id)]]);   // A:C
      sh.getRange(r, 5).setValue(Number(it.qty) || 0);                              // E
      sh.getRange(r, 8, 1, 5).setValues([[
        mode,
        String(d.place || ''),
        i === 0 ? (Number(d.ship) || 0) : '',   // phí ship chỉ ghi ở dòng đầu của đơn
        'Mới',
        note
      ]]);                                                                           // H:L
    });
    return out({ ok: true, orderId: orderId });
  } catch (err) {
    return out({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

function doGet() {
  return out({ ok: true, msg: 'DUYNPAO order hook đang chạy' });
}

function out(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
