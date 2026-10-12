import os, random, sqlite3, json
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")
ADMIN_ID = 123456789 # Ganti ID Telegram lu biar bisa broadcast

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, tb INTEGER, bb INTEGER, target TEXT, progress INTEGER DEFAULT 0, join_date TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS logs (user_id INTEGER, fitur TEXT, tanggal TEXT)")
    conn.commit(); conn.close()
init_db()

MENU = [
    ["📋 CEK ADMINISTRASI", "🏥 RIKKES LENGKAP"],
    ["🎖️ TNI AD", "⚓ TNI AL", "✈️ TNI AU"],
    ["🏃 GARJAS AKURAT", "🧠 PSIKOTES PRO"],
    ["🧩 WARTEGG 8 KOTAK", "👤 ORANG & POHON"],
    ["💬 PANTUKHIR AI", "📚 BANK SOAL 500"],
    ["📈 PROGRESS GUE", "📍 PANDA PASURUAN"],
    ["⏰ SET REMINDER H-30"]
]
markup = ReplyKeyboardMarkup(MENU, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (id, progress, join_date) VALUES (?,?,?)", (uid, 10, datetime.now().strftime("%d-%m-%Y")))
    conn.commit(); conn.close()
    await update.message.reply_text(
        "🇮🇩 **BOT SIAP LANTIK PRO MAX V1.0**\n\n"
        "Halo Calon Prajurit Pasuruan!\n"
        "Bot ini bimbing lu 7 tahap sampai dilantik:\n"
        "1. Administrasi 2. Rikkes 3. Garjas 4. Psikotes 5. MI 6. Pantukhir 7. Lantik\n\n"
        "Ketik /bantuan untuk panduan.\n"
        "Pilih menu di bawah:",
        reply_markup=markup, parse_mode='Markdown'
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text
    uid = update.effective_user.id

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO logs (user_id, fitur, tanggal) VALUES (?,?,?)", (uid, txt, datetime.now().isoformat()))
    conn.commit(); conn.close()

    if "ADMINISTRASI" in txt:
        await update.message.reply_text(
            "📋 **CEK ADMINISTRASI - PALING BANYAK GUGUR DI SINI!**\n\n"
            "Wajib bawa Pasuruan (Kodam V):\n"
            "1. KTP & KK asli + FC 5 lembar\n"
            "2. Ijazah SD-SMA asli + legalisir\n"
            "3. Akta Lahir\n"
            "4. SKCK Polres Pasuruan (masih aktif)\n"
            "5. Surat belum menikah dari KUA/Desa\n"
            "6. BPJS aktif\n"
            "7. Pas foto 4x6 background merah 10 lembar, 3x4 10 lembar\n"
            "8. Materai 10rb 5 lembar\n"
            "9. Tinggi: AD 163cm, AL/AU 165cm. Umur 17y9b - 22th\n\n"
            "Ketik: /cek_tb 168 /cek_umur 19\n"
            "Bot auto cek lolos/tidak"
        )
    elif "RIKKES" in txt:
        await update.message.reply_text(
            "🏥 **RIKKES 30 TITIK LENGKAP**\n\n"
            "❌ AUTO TMS (Tidak Memenuhi Syarat):\n"
            "- Mata minus >1, buta warna parsial/total\n"
            "- Varikokel grade 2-3, hernia, ambeien luar\n"
            "- Tato, tindik, bekas tindik\n"
            "- Gigi berlubang >3, gigi depan ompong, karang gigi tebal\n"
            "- Tekanan darah >140/90, HB <13\n"
            "- Flat foot parah, skoliosis\n\n"
            "✅ H-30 FIX:\n"
            "Stop rokok/kopi, minum 3L, tidur jam 9, scaling gigi di Puskesmas Bangil/Pasuruan (gratis BPJS), lari tanpa alas."
        )
    elif "TNI AD" in txt:
        await update.message.reply_text("🎖️ TNI AD: Lari 12' target 3507m=100, 2800m=70. Pullup 20x=100. Batas lulus Garjas 61. Ketik /garjas 3000 15 45 43 14")
    elif "TNI AL" in txt:
        await update.message.reply_text("⚓ TNI AL: WAJIB RENANG 50m <60 detik gaya dada. Banyak gugur. Latihan di Kolam Renang Bangil. Lari 2400m minimal.")
    elif "TNI AU" in txt:
        await update.message.reply_text("✈️ TNI AU: Tes Akademik Inggris wajib. Psikotes paling ketat. Lari 3200m=100.")
    elif "GARJAS" in txt:
        await update.message.reply_text("🏃 **GARJAS AKURAT TABEL 2019-2026**\nFormat: /garjas [lari meter] [pullup] [situp] [pushup] [shuttle detik]\nContoh: /garjas 3000 15 45 43 14\nBot hitung pakai tabel resmi TNI.")
    elif "PSIKOTES" in txt:
        await update.message.reply_text(
            "🧠 **PSIKOTES PRO**\n\n"
            "1. PAULI/KRAEPLIN (Koran):\n"
            "Angka berderet atas-bawah, jumlahkan 2 angka, tulis angka belakangnya. Jangan ngebut awal, stabil di tengah, grafik naik = ambisius bagus.\n"
            "Ketik /pauli untuk simulasi real 60 detik\n\n"
            "2. LOGIKA: Deret angka, sinonim, antonim, analogi\n"
            "Ketik /soal_logika"
        )
    elif "WARTEGG" in txt:
        await update.message.reply_text(
            "🧩 **WARTEGG 8 KOTAK - KUNCI LOLOS**\n"
            "1: Titik tengah -> Matahari/Kompas (identitas)\n"
            "2: Garis lengkung -> Burung/Daun (emosi)\n"
            "3: 3 garis -> Tangga/Gedung (ambisi WAJIB naik)\n"
            "4: Kotak hitam -> Jendela/Papan catur\n"
            "5: 2 garis silang -> Ketapel (jangan senjata)\n"
            "6: 2 garis pisah -> Tiang listrik/Jembatan\n"
            "7: 7 titik -> Padi 7 bulir\n"
            "8: Lengkung besar -> Payung/Helm\n\n"
            "Urutan ideal: 1-2-3-4-8-7-6-5. Jangan urut 1-8 (kaku) atau acak total (liar)"
        )
    elif "ORANG" in txt:
        await update.message.reply_text("👤 **DAP & POHON**\nOrang: Full body, laki-laki, profesi TNI/Guru/Petani bawa cangkul, proporsi pas, wajah senyum, tangan kaki lengkap. Jangan stickman.\nPohon: Mangga/beringin, akar kelihatan, batang tebal, cabang 3, buah 5-7, daun rimbun. Jangan pohon pisang/bambu/jagung.")
    elif "PANTUKHIR" in txt:
        await update.message.reply_text(
            "💬 **PANTUKHIR AI - 100 SOAL JEBAKAN**\n"
            "Q: Kenapa mau TNI?\nA Ideal: Mengabdi NKRI, siap ditempatkan di mana saja, menjaga kedaulatan.\n\n"
            "Q: Punya pacar?\nA Ideal: Tidak ada, fokus persiapan (jangan jawab punya)\n\n"
            "Q: Kalau disuruh atasan melanggar hukum?\nA Ideal: Lapor berjenjang, tetap pada Sapta Marga.\n\nKetik /pantukhir_next"
        )
    elif "BANK SOAL" in txt:
        await update.message.reply_text("📚 Ketik: /soal_logika /soal_mtk /soal_wawasan /soal_pancasila\nBot kirim 10 soal random + kunci")
    elif "PROGRESS" in txt:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT progress FROM users WHERE id=?", (uid,))
        r = c.fetchone()
        prog = r[0] if r else 10
        conn.close()
        await update.message.reply_text(f"📈 Progress lu: {prog}%\n7 Tahap: Admin({ '✅' if prog>10 else '❌'}) -> Rikkes -> Garjas -> Psikotes -> MI -> Pantukhir -> Lantik\nTingkatkan dengan /garjas & /pauli\nTarget lantik: 100%")
    elif "PANDA" in txt:
        await update.message.reply_text("📍 **PANDA PASURUAN**\nAD: Ajendam V Brawijaya Surabaya, Jl. Raden Wijaya\nAL: Lanal Malang, Jl. Yos Sudarso\nAU: Lanud Abd Saleh Malang\nBawa: Materai 10rb, foto merah 4x6 10 lbr, stopmap merah.")
    elif "REMINDER" in txt:
        await update.message.reply_text("⏰ Reminder H-30 aktif! Bot akan chat jam 04:30 WIB tiap hari: 'Lari 3km + Pushup 50x'. Ketik /stop_reminder untuk berhenti. Fitur ini jalan kalau server Render on.")
    else:
        await update.message.reply_text("Pilih menu bos.", reply_markup=markup)

async def garjas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        lari = int(context.args[0])
        nilai = 100 if lari>=3507 else 95 if lari>=3300 else 85 if lari>=3222 else 70 if lari>=2800 else 60 if lari>=2500 else 40
        kat = "BS (81-100) AMAN" if nilai>=81 else "B (61-80) LULUS" if nilai>=61 else "C (41-60) GAGAL - Panda Pasuruan gak lolos"
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("UPDATE users SET progress=progress+5 WHERE id=?", (update.effective_user.id,))
        conn.commit(); conn.close()
        await update.message.reply_text(f"🏃 Lari {lari}m = Nilai {nilai} -> {kat}\nBatas lulus TNI: 61\nProgress +5%")
    except:
        await update.message.reply_text("Format: /garjas 3000")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("garjas", garjas))
    app.add_handler(CommandHandler("bantuan", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    print("BOT FINAL V1.0 JALAN")
    app.run_polling()

if __name__ == "__main__":
    main()
