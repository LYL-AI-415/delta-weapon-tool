import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

# ==================== 完整枪械数据库 ====================
WEAPON_DB = {
    "M4A1": {"type": "突击步枪", "适合": "均衡中距离", "后坐力": 3, "射速": 3, "伤害": 2, "风格标签": "均衡 远射 稳定"},
    "MP5":  {"type": "冲锋枪",   "适合": "近战高速", "后坐力": 1, "射速": 5, "伤害": 1, "风格标签": "腰射 跑打 消音"},
    "AK-47":{"type": "突击步枪", "适合": "高伤压枪", "后坐力": 5, "射速": 2, "伤害": 4, "风格标签": "压枪 远程点射"},
    "AWM":  {"type": "狙击步枪", "适合": "一击致命", "后坐力": 5, "射速": 1, "伤害": 5, "风格标签": "瞬狙 超远 消音"},
    "M700": {"type": "射手步枪", "适合": "灵活狙击", "后坐力": 4, "射速": 2, "伤害": 4, "风格标签": "连狙 性价比"},
    "SR3M": {"type": "冲锋枪",   "适合": "撕咬双修", "后坐力": 2, "射速": 4, "伤害": 2, "风格标签": "腰射 双修 撕咬"},
    "KC17": {"type": "射手步枪", "适合": "远距压制", "后坐力": 3, "射速": 2, "伤害": 4, "风格标签": "长管 短管 倍镜"},
    "MK47（余烬）": {"type": "突击步枪", "适合": "均衡影袭", "后坐力": 3, "射速": 3, "伤害": 3, "风格标签": "均衡 消音 影袭 CT"},
    "RM277": {"type": "狙击步枪", "适合": "重型高伤", "后坐力": 4, "射速": 1, "伤害": 5, "风格标签": "重型 倍镜 性价比"},
    "AKM（颗秒）": {"type": "突击步枪", "适合": "暴力压枪", "后坐力": 5, "射速": 2, "伤害": 4, "风格标签": "压枪 低价 沙暴"},
    "ASH12": {"type": "射手步枪", "适合": "双发双修", "后坐力": 3, "射速": 2, "伤害": 4, "风格标签": "腰射 双修 开镜"},
    "MK4（全自动）": {"type": "冲锋枪", "适合": "全自动腰射", "后坐力": 2, "射速": 5, "伤害": 1, "风格标签": "腰射 高机动"},
    "K437": {"type": "突击步枪", "适合": "双流顶配", "后坐力": 3, "射速": 3, "伤害": 3, "风格标签": "CT 骨架 顶配"},
    "M14": {"type": "射手步枪", "适合": "共振系列", "后坐力": 3, "射速": 2, "伤害": 4, "风格标签": "共振 CT 影袭 弹鼓"},
    "M7":  {"type": "射手步枪", "适合": "CT消音顶配", "后坐力": 3, "射速": 2, "伤害": 4, "风格标签": "CT 消音 共振 锚点"},
    "MP7（月影）": {"type": "冲锋枪", "适合": "极限双修", "后坐力": 2, "射速": 5, "伤害": 2, "风格标签": "腰射 射程 短管"},
    "腾龙": {"type": "突击步枪", "适合": "双水平满改", "后坐力": 3, "射速": 3, "伤害": 3, "风格标签": "UR CT 双水平"},
}

HOT_CODES = {
    "M4A1": [("激光远射流", "M4A1-X8K2PL9W", "中远距离，后坐力极低"),
             ("近战腰射王", "M4A1-C3M7QY1V", "室内腰射精度极高"),
             ("全能平衡", "M4A1-T5R9BN6L", "开镜快，适合跑打"),
             ("稳如磐石", "M4A1-J2H4FG0D", "蹲点架枪")],
    "MP5": [("无脑腰射", "MP5-R7U3EP5S", "贴脸腰射无敌"),
            ("跑打鬼畜", "MP5-K4W2MN8X", "移动开镜惩罚极小"),
            ("消音渗透", "MP5-A9Q1BZ3Y", "绕后偷人")],
    "AK-47": [("暴力压枪", "AK47-G6T0VN4I", "近中距离爆发"),
              ("远程单点", "AK47-L8P2CX7O", "高倍镜单点"),
              ("丐版战神", "AK47-Z5R1ME9W", "便宜好用")],
    "AWM": [("瞬狙快切", "AWM-U3S7QF2D", "开镜极快"),
            ("超远狙击", "AWM-Y6E0HJ1K", "15倍镜"),
            ("消音幽灵", "AWM-V4B8NP3M", "消音拉栓")],
    "M700": [("平民神狙", "M700-D2W5XL6T", "性价比极高"),
             ("连狙压制", "M700-H8K3RC9Q", "半自动火力")],
    "SR3M": [("双修顶配版（射程腰射）", "6K25SBS0EU90O684D8QL5", "远近兼顾"),
             ("双修顶配版（极限射程）", "6K25SL40EU90O684D8QL5", "极限射程"),
             ("性价比撕咬版", "6K26PBC0B1RRH96DI8AIT", "25万"),
             ("高改撕咬版", "6K26OH0049H3TLFDHMKHO", "35万")],
    "KC17": [("超性价比版", "6KI9THS0EU90O684D8QL5", "30万"),
             ("短管高改版", "6KI9U5O0EU90O684D8QL5", "42万"),
             ("短管FFC顶配版", "6KI9V3C0EU90O684D8QL5", "55万"),
             ("长管密令沙暴顶配版", "6KI9V9C0EU90O684D8QL5", "55万"),
             ("长管FFC倍镜版", "6KIA01C0EU90O684D8QL5", "60万"),
             ("长管密令沙暴倍镜版", "6KI9VQG0EU90O684D8QL5", "60万")],
    "MK47（余烬）": [("共二主宰版（均衡稳定）", "6KIVVQO049H3TLFDHMKHO", "均衡"),
                  ("共振影袭版（上手简单）", "6KJ01S4049H3TLFDHMKHO", "新手"),
                  ("相位CT版（正据枪）", "6KJ029G049H3TLFDHMKHO", "CT据枪"),
                  ("消音版幻影主宰版", "6KJ04P0049H3TLFDHMKHO", "消音"),
                  ("消音版共一影袭版", "6KJ0520049H3TLFDHMKHO", "消音影袭")],
    "RM277": [("重型一体超性价比版", "6KO8LD40EU90O684D8QL5", "24万"),
              ("重型一体中改加强版", "6KO9OIG0B1RRH96DI8AIT", "28万可改倍镜"),
              ("重型一体高改版", "6KO9ODO0B1RRH96DI8AIT", "34万可改倍镜")],
    "AKM（颗秒）": [("纯粹粑粑版", "6KOT7FO0EU90O684D8QL5", "18万"),
                  ("强化粑粑版", "6KOT84K0EU90O684D8QL5", "加强"),
                  ("满改A版（沙暴锚点）", "6KOT8T80EU90O684D8QL5", "30万"),
                  ("满改B版（俄消UR）", "6KOTQBS0B1RRH96DI8AIT", "30万")],
    "ASH12": [("双发腰射双修版（15精校）", "6KHV6TC049H3TLFDHMKHO", "腰射双修"),
              ("双发共振开镜版（0/30精校）", "6KHV6VS049H3TLFDHMKHO", "开镜流"),
              ("常规满改（共振二代）", "6K4QSNC0B1RRH96DI8AIT", "共振"),
              ("常规满改（幻影握把）", "6K4QSR80B1RRH96DI8AIT", "幻影")],
    "MK4（全自动）": [("腰射性价比版", "6K3QSVO049H3TLFDHMKHO", "25万"),
                   ("腰射中改版（QR枪托）", "6K3QSH0049H3TLFDHMKHO", "32万"),
                   ("腰射中改版（EC阻手）", "6K3QSMO049H3TLFDHMKHO", "33万"),
                   ("腰射高改版（最准腰射）", "6K3QT3K049H3TLFDHMKHO", "37万")],
    "K437": [("双流骨架究极顶配版", "6K44FU4049H3TLFDHMKHO", "45万"),
             ("双流CT究极顶配版", "6K45BC0049H3TLFDHMKHO", "45万"),
             ("双垂直究极顶配版", "6K44G5K049H3TLFDHMKHO", "45万"),
             ("倍镜高改版", "6K44GP4049H3TLFDHMKHO", "38万"),
             ("均衡高改版", "6K44HB0049H3TLFDHMKHO", "35万")],
    "M14": [("新共振三代稳定型", "6JR7PJ40B0GKDDOTE9T6Q", "稳定"),
            ("新共振三代高操控", "6JR7QJ80B0GKDDOTE9T6Q", "高操控"),
            ("共振人体CT托版", "6JR7RNG0B0GKDDOTE9T6Q", "CT托"),
            ("共振人体影袭版", "6JR7RUO0B0GKDDOTE9T6Q", "影袭"),
            ("共振二代标准版", "6JR7SPS0B0GKDDOTE9T6Q", "标准"),
            ("共振二代弹鼓版", "6JR7T000B0GKDDOTE9T6Q", "弹鼓")],
    "M7": [("双流CT顶配版", "6JQJDAK0BAC7RIM3B0293", "CT顶配"),
           ("消音CT顶配版", "6JQJDMS0BAC7RIM3B0293", "消音CT"),
           ("共振二代顶配版", "6JQJE200BAC7RIM3B0293", "共振二代"),
           ("共振二代锚点版", "6JQKCVO0B0GKDDOTE9T6Q", "锚点")],
    "MP7（月影）": [("极限腰射双修顶配", "6JVHO400E0LL9IRHUI52L", "腰射双修"),
                 ("极限射程双修顶配", "6JVHOKG0E0LL9IRHUI52L", "射程双修"),
                 ("短管极限腰射顶配", "6JVREE40B0GKDDOTE9T6Q", "短管腰射"),
                 ("增强枪管双修顶配", "6JVRF600B0GKDDOTE9T6Q", "增强双修")],
    "腾龙": [("经典UR双水平满改（30发）", "6K1HVGK049H3TLFDHMKHO", "30发"),
             ("S9推荐CT双水平满改（30发）", "6K1HVO4049H3TLFDHMKHO", "30发"),
             ("S9推荐CT双水平满改（45发）", "6K1I0DG049H3TLFDHMKHO", "45发")],
    "MK47（鏖战）": [("无后坐BUG改法A（快速开镜）", "6JU5M3G0EU90O684D8QL5", "快速开镜"),
                  ("无后坐BUG改法B（极限稳定）", "6JU5OF40EU90O684D8QL5", "极限稳定"),
                  ("腰射双修A", "6JU6UUC0EU90O684D8QL5", "腰射双修A"),
                  ("腰射双修B", "6JU6V2G0EU90O684D8QL5", "腰射双修B")],
}

# ==================== 界面配色 ====================
BG = "#F5F6FA"
CARD_BG = "#FFFFFF"
ACCENT = "#2C3E50"
BTN_COLOR = "#3498DB"
BTN_TEXT = "white"
FONT = "微软雅黑"

class ModernWeaponAdvisor:
    def __init__(self, root):
        self.root = root
        self.root.title("三角洲行动 · 枪械私人顾问 Pro")
        self.root.geometry("800x900")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        # 样式
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", background=BG, font=(FONT, 10))
        style.configure("TLabelframe", background=BG, font=(FONT, 10, "bold"))
        style.configure("TLabelframe.Label", background=BG)
        style.configure("TButton", font=(FONT, 10), padding=6)
        style.configure("Card.TFrame", background=CARD_BG, relief="solid", borderwidth=1)
        style.configure("Accent.TButton", background=BTN_COLOR, foreground=BTN_TEXT)
        style.map("Accent.TButton", background=[("active", "#2980B9")])

        # 变量
        self.dpi = tk.IntVar(value=800)
        self.reaction_time = tk.DoubleVar(value=250.0)
        self.dpi_measurements = []
        self.pref_type = tk.StringVar(value="自动选择")
        self.pref_range = tk.StringVar(value="中距离")
        self.pref_style = tk.StringVar(value="均衡")
        self.pref_recoil = tk.StringVar(value="垂直优先")
        self.pref_suppressor = tk.BooleanVar(value=False)
        self.pref_hipfire = tk.BooleanVar(value=False)
        self.pref_scope = tk.StringVar(value="红点/全息")
        self.pad_size = tk.StringVar(value="中号（30-40cm）")
        self.screen_res = tk.StringVar(value="1920x1080")
        self.in_game_sens = tk.DoubleVar(value=1.0)

        # 查询筛选
        self.filter_type = tk.StringVar(value="全部")
        self.filter_style_keyword = tk.StringVar(value="")
        self.selected_weapon = tk.StringVar(value="M4A1")

        self.create_ui()

    def create_ui(self):
        # 主容器
        main = ttk.Frame(self.root, padding=15)
        main.pack(fill="both", expand=True)

        # 标题
        title = tk.Label(main, text="三角洲行动 · 枪械私人顾问 Pro",
                         font=(FONT, 18, "bold"), fg=ACCENT, bg=BG)
        title.pack(pady=(0,10))

        # 笔记本
        nb = ttk.Notebook(main)
        nb.pack(fill="both", expand=True)

        # 四个选项卡
        nb.add(self.dpi_tab(), text="① DPI 测试")
        nb.add(self.rt_tab(), text="② 反应速度")
        nb.add(self.pref_tab(), text="③ 战斗偏好")
        nb.add(self.result_tab(), text="④ 智能推荐 & 风格查询")

        # 底部按钮
        btn_bar = ttk.Frame(main)
        btn_bar.pack(pady=15)
        ttk.Button(btn_bar, text="🔍 综合分析生成推荐", style="Accent.TButton",
                   command=self.full_analyze).pack(side="left", padx=10)
        ttk.Button(btn_bar, text="📋 按风格筛选查询", style="Accent.TButton",
                   command=self.filtered_query).pack(side="left", padx=10)

    def dpi_tab(self):
        tab = ttk.Frame(padding=15)
        card = ttk.Frame(tab, style="Card.TFrame", padding=20)
        card.pack(fill="both", expand=True)

        ttk.Label(card, text="📏 精准 DPI 测量（A4纸辅助法）", font=(FONT, 13, "bold")).pack()
        ttk.Label(card, text="将鼠标放在纸左边，按住左键水平移动到右边（21cm），重复3次。",
                  foreground="gray", font=(FONT, 9)).pack(pady=5)

        self.dpi_canvas = tk.Canvas(card, height=45, bg="#D5D8DC", highlightthickness=0)
        self.dpi_canvas.pack(fill="x", pady=10)
        self.dpi_canvas.bind("<Button-1>", self.start_dpi)
        self.dpi_canvas.bind("<B1-Motion>", self.update_dpi)
        self.dpi_canvas.bind("<ButtonRelease-1>", self.end_dpi)

        self.dpi_status = ttk.Label(card, text="按住左键滑动，松开后记录", foreground="gray")
        self.dpi_status.pack()
        self.dpi_progress = ttk.Label(card, text="已完成 0/3 次", font=(FONT, 10, "bold"))
        self.dpi_progress.pack(pady=5)

        val = ttk.Frame(card)
        val.pack(fill="x", pady=10)
        ttk.Label(val, text="当前平均 DPI：").pack(side="left")
        ttk.Label(val, textvariable=self.dpi, foreground="#E74C3C", font=(FONT, 14, "bold")).pack(side="left")
        ttk.Button(val, text="手动输入", command=self.manual_dpi).pack(side="right", padx=5)
        ttk.Button(val, text="重置", command=self.reset_dpi).pack(side="right")
        return tab

    def rt_tab(self):
        tab = ttk.Frame(padding=15)
        card = ttk.Frame(tab, style="Card.TFrame", padding=25)
        card.pack(fill="both", expand=True)
        ttk.Label(card, text="🧠 反应速度测试", font=(FONT, 13, "bold")).pack(pady=10)
        self.rt_btn = tk.Button(card, text="开始反应测试（共5次）", bg="#7F8C8D", fg="white",
                                font=(FONT, 14, "bold"), relief="flat", padx=30, pady=12,
                                command=self.start_rt)
        self.rt_btn.pack(pady=25)
        ttk.Label(card, text="平均反应时间(ms)：").pack(side="left")
        ttk.Label(card, textvariable=self.reaction_time, foreground="#E74C3C", font=(FONT, 14, "bold")).pack(side="left")
        return tab

    def pref_tab(self):
        tab = ttk.Frame(padding=15)
        # 用两个卡片上下排列
        card1 = ttk.Frame(tab, style="Card.TFrame", padding=15)
        card1.pack(fill="x", pady=5)
        ttk.Label(card1, text="基本偏好", font=(FONT, 11, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=5)
        ttk.Label(card1, text="武器类型：").grid(row=1, column=0, sticky="w", padx=5, pady=3)
        ttk.Combobox(card1, textvariable=self.pref_type, values=["自动选择","突击步枪","冲锋枪","狙击步枪","射手步枪"],
                     state="readonly", width=20).grid(row=1, column=1, padx=5)
        ttk.Label(card1, text="交战距离：").grid(row=2, column=0, sticky="w", padx=5, pady=3)
        ttk.Combobox(card1, textvariable=self.pref_range, values=["近距离","中距离","远距离","混合"],
                     state="readonly", width=20).grid(row=2, column=1, padx=5)
        ttk.Label(card1, text="射击风格：").grid(row=3, column=0, sticky="w", padx=5, pady=3)
        ttk.Combobox(card1, textvariable=self.pref_style, values=["泼水/扫射","快速点射","单点精准","均衡"],
                     state="readonly", width=20).grid(row=3, column=1, padx=5)

        card2 = ttk.Frame(tab, style="Card.TFrame", padding=15)
        card2.pack(fill="x", pady=5)
        ttk.Label(card2, text="操作与配件", font=(FONT, 11, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=5)
        ttk.Label(card2, text="压枪习惯：").grid(row=1, column=0, sticky="w", padx=5, pady=3)
        ttk.Combobox(card2, textvariable=self.pref_recoil, values=["垂直优先","水平优先","无脑压枪","微控点射"],
                     state="readonly", width=20).grid(row=1, column=1, padx=5)
        ttk.Label(card2, text="瞄具偏好：").grid(row=2, column=0, sticky="w", padx=5, pady=3)
        ttk.Combobox(card2, textvariable=self.pref_scope, values=["红点/全息","2-4倍镜","高倍镜(6倍以上)","机瞄/无"],
                     state="readonly", width=20).grid(row=2, column=1, padx=5)
        ttk.Checkbutton(card2, text="偏爱消音器", variable=self.pref_suppressor).grid(row=3, column=0, sticky="w", padx=5, pady=3)
        ttk.Checkbutton(card2, text="偏爱腰射握把", variable=self.pref_hipfire).grid(row=3, column=1, sticky="w", padx=5, pady=3)

        card3 = ttk.Frame(tab, style="Card.TFrame", padding=15)
        card3.pack(fill="x", pady=5)
        ttk.Label(card3, text="外设环境", font=(FONT, 11, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=5)
        ttk.Label(card3, text="鼠标垫：").grid(row=1, column=0, sticky="w", padx=5, pady=3)
        ttk.Combobox(card3, textvariable=self.pad_size, values=["小号(<30cm)","中号（30-40cm）","大号（40-50cm）","桌垫级(>50cm)"],
                     state="readonly", width=20).grid(row=1, column=1, padx=5)
        ttk.Label(card3, text="分辨率：").grid(row=2, column=0, sticky="w", padx=5, pady=3)
        ttk.Combobox(card3, textvariable=self.screen_res, values=["1920x1080","2560x1440","3840x2160","1366x768"],
                     state="readonly", width=20).grid(row=2, column=1, padx=5)
        ttk.Label(card3, text="游戏灵敏度：").grid(row=3, column=0, sticky="w", padx=5, pady=3)
        sens_frame = ttk.Frame(card3)
        sens_frame.grid(row=3, column=1, padx=5)
        ttk.Entry(sens_frame, textvariable=self.in_game_sens, width=10).pack(side="left")
        ttk.Label(sens_frame, text="（例：1.0）").pack(side="left")
        return tab

    def result_tab(self):
        tab = ttk.Frame(padding=15)
        # 筛选卡片
        filter_card = ttk.Frame(tab, style="Card.TFrame", padding=10)
        filter_card.pack(fill="x", pady=5)
        ttk.Label(filter_card, text="🔍 风格筛选查询", font=(FONT, 11, "bold")).grid(row=0, column=0, columnspan=4, sticky="w", pady=5)
        ttk.Label(filter_card, text="类型：").grid(row=1, column=0, padx=5, pady=3)
        ttk.Combobox(filter_card, textvariable=self.filter_type, values=["全部","突击步枪","冲锋枪","狙击步枪","射手步枪"],
                     state="readonly", width=15).grid(row=1, column=1, padx=5)
        ttk.Label(filter_card, text="风格关键词：").grid(row=1, column=2, padx=5, pady=3)
        ttk.Entry(filter_card, textvariable=self.filter_style_keyword, width=18).grid(row=1, column=3, padx=5)
        ttk.Button(filter_card, text="执行筛选", style="Accent.TButton", command=self.filtered_query).grid(row=1, column=4, padx=10)

        # 结果显示
        self.result_text = tk.Text(tab, height=24, width=90, font=(FONT, 10), wrap="word",
                                   bg="white", relief="solid", bd=1)
        self.result_text.pack(fill="both", expand=True, pady=5)
        return tab

    # ==================== 功能逻辑 ====================
    def start_dpi(self, event):
        self.dpi_testing = True
        self.dpi_start_x = event.x
        self.dpi_pixel_moved = 0
        self.dpi_canvas.config(bg="#E67E22")

    def update_dpi(self, event):
        if self.dpi_testing:
            self.dpi_pixel_moved = abs(event.x - self.dpi_start_x)

    def end_dpi(self, event):
        if not self.dpi_testing: return
        self.dpi_testing = False
        self.dpi_canvas.config(bg="#D5D8DC")
        if self.dpi_pixel_moved < 50:
            messagebox.showwarning("无效", "移动距离太短，请划过整张纸（21cm）")
            return
        dpi_val = int(self.dpi_pixel_moved / 8.2677)
        dpi_val = max(100, min(12000, dpi_val))
        self.dpi_measurements.append(dpi_val)
        n = len(self.dpi_measurements)
        self.dpi_progress.config(text=f"已完成 {n}/3 次")
        self.dpi_status.config(text=f"第{n}次：{dpi_val} DPI")
        if n >= 3:
            avg = sum(self.dpi_measurements) / n
            self.dpi.set(round(avg))
            self.dpi_status.config(text=f"平均 DPI：{round(avg)}")
            self.dpi_measurements.clear()
            self.dpi_progress.config(text="测量完成！可重新测试")
        else:
            self.dpi_status.config(text=f"还剩 {3-n} 次测量")

    def manual_dpi(self):
        win = tk.Toplevel(self.root)
        win.title("手动输入 DPI")
        win.configure(bg=BG)
        ttk.Label(win, text="请输入鼠标 DPI（100-12000）").pack(padx=20, pady=10)
        entry = ttk.Entry(win)
        entry.pack(padx=20)
        def set_dpi():
            try:
                val = int(entry.get())
                if 100 <= val <= 12000:
                    self.dpi.set(val)
                    self.dpi_measurements.clear()
                    self.dpi_progress.config(text="已手动设定")
                    win.destroy()
                else:
                    messagebox.showwarning("错误", "范围 100-12000")
            except:
                messagebox.showwarning("错误", "请输入整数")
        ttk.Button(win, text="确定", command=set_dpi).pack(pady=10)

    def reset_dpi(self):
        self.dpi_measurements.clear()
        self.dpi_progress.config(text="已重置，重新测3次")
        self.dpi_status.config(text="按住左键从纸左边划到右边")

    def start_rt(self):
        self.rt_btn.config(state="disabled", text="等待绿色...", bg="#7F8C8D")
        self.root.update()
        delay = random.randint(1000, 3000)
        self.root.after(delay, self.show_green)

    def show_green(self):
        self.rt_btn.config(bg="#2ECC71", text="点击！！！", state="normal")
        self.rt_start = time.time()
        self.rt_btn.config(command=self.record_rt)

    def record_rt(self):
        rt = (time.time() - self.rt_start) * 1000
        if not hasattr(self, 'rt_list'):
            self.rt_list = []
        self.rt_list.append(rt)
        self.rt_btn.config(bg="#7F8C8D", text="继续测试", command=self.start_rt)
        if len(self.rt_list) >= 5:
            avg = sum(self.rt_list) / len(self.rt_list)
            self.reaction_time.set(round(avg, 1))
            self.rt_btn.config(bg="#95A5A6", text="测试完成", state="disabled", command=None)
            messagebox.showinfo("反应测试", f"5次平均：{avg:.1f} ms")
            self.rt_list = []

    # ==================== 筛选查询 ====================
    def filtered_query(self):
        wtype = self.filter_type.get()
        keyword = self.filter_style_keyword.get().strip().lower()
        results = []
        for name, codes in HOT_CODES.items():
            info = WEAPON_DB.get(name, {})
            if wtype != "全部" and info.get("type") != wtype:
                continue
            # 风格标签匹配
            tags = info.get("风格标签", "").lower()
            if keyword and keyword not in tags and keyword not in name.lower():
                # 也检查改枪码名称
                match_code = any(keyword in c[0].lower() for c in codes)
                if not match_code:
                    continue
            results.append((name, info.get("适合", ""), codes))

        if not results:
            output = "没有找到匹配的枪械，请尝试更换关键词或类型。"
        else:
            output = ""
            for name, suit, codes in results:
                output += f"【{name}】（{suit}）\n"
                for cname, code, desc in codes:
                    output += f"  • {cname}\n    码：{code}\n    说明：{desc}\n"
                output += "\n"
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, output)

    # ==================== 智能推荐 ====================
    def full_analyze(self):
        dpi = self.dpi.get()
        rt = self.reaction_time.get()
        pref_type = self.pref_type.get()
        pref_range = self.pref_range.get()
        pref_style = self.pref_style.get()
        recoil = self.pref_recoil.get()
        supp = self.pref_suppressor.get()
        hipfire = self.pref_hipfire.get()
        scope = self.pref_scope.get()
        pad = self.pad_size.get()
        res = self.screen_res.get()
        sens = self.in_game_sens.get()

        # 候选枪
        candidates = list(WEAPON_DB.keys())
        if pref_type != "自动选择":
            type_map = {
                "突击步枪": ["M4A1","AK-47","MK47（余烬）","MK47（鏖战）","K437","腾龙","AKM（颗秒）"],
                "冲锋枪": ["MP5","SR3M","MK4（全自动）","MP7（月影）"],
                "狙击步枪": ["AWM","RM277"],
                "射手步枪": ["M700","KC17","ASH12","M14","M7"],
            }
            candidates = [w for w in type_map.get(pref_type, []) if w in WEAPON_DB]
            if not candidates:
                candidates = list(WEAPON_DB.keys())

        # 综合评分
        scores = {}
        for w in candidates:
            s = 0
            stat = WEAPON_DB[w]
            # 基础匹配
            if dpi >= 800:
                s += stat["射速"] * 3
            else:
                s += (6 - stat["后坐力"]) * 3
            if rt <= 200:
                if stat["type"] in ["冲锋枪","突击步枪"]:
                    s += 8
            else:
                if stat["type"] in ["狙击步枪","射手步枪"]:
                    s += 8
            if pref_range == "近距离" and stat["type"] == "冲锋枪":
                s += 15
            elif pref_range == "远距离" and stat["type"] in ["狙击步枪","射手步枪"]:
                s += 15
            elif pref_range == "中距离" and stat["type"] == "突击步枪":
                s += 12

            # 风格与配件匹配
            tags = stat["风格标签"].lower()
            if hipfire and "腰射" in tags:
                s += 10
            if supp and "消音" in tags:
                s += 8
            if scope in ["高倍镜(6倍以上)"] and ("倍镜" in tags or "远射" in tags):
                s += 8
            if recoil in ["垂直优先","水平优先"] and ("稳定" in tags or "均衡" in tags):
                s += 5
            scores[w] = s

        best = max(scores, key=scores.get) if scores else "M4A1"

        # 从 best 的码中挑选最匹配
        codes = HOT_CODES.get(best, [])
        best_match = codes[0] if codes else ("默认", "N/A", "")
        best_match_score = -1
        for name, code, desc in codes:
            ms = 0
            if hipfire and "腰射" in name:
                ms += 10
            if supp and "消音" in name:
                ms += 10
            if "顶配" in name:
                ms += 3
            if pref_range == "近距离" and ("腰射" in name or "跑打" in name):
                ms += 8
            if pref_range == "远距离" and ("远射" in name or "倍镜" in name):
                ms += 8
            if ms > best_match_score:
                best_match_score = ms
                best_match = (name, code, desc)

        output = f"""【用户画像】
DPI：{dpi}  |  反应：{rt} ms
类型偏好：{pref_type}  |  距离：{pref_range}  |  风格：{pref_style}
压枪：{recoil}  |  瞄具：{scope}
消音：{'是' if supp else '否'}  |  腰射握把：{'是' if hipfire else '否'}
鼠标垫：{pad}  |  分辨率：{res}  |  灵敏度：{sens}

【智能推荐】
枪械：{best} ({WEAPON_DB[best]['type']})
特点：{WEAPON_DB[best]['适合']}

【最佳匹配改枪码】
改装名称：{best_match[0]}
改枪码：{best_match[1]}
适用说明：{best_match[2]}
（来自聪聪实测方案）
"""
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, output)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernWeaponAdvisor(root)
    root.mainloop()
