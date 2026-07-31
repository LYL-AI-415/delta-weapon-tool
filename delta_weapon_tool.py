import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
import string

# ==================== 枪械数据库（模拟《三角洲行动》） ====================
WEAPON_DB = {
    "M4A1": {
        "type": "突击步枪",
        "base_stats": {"伤害": 35, "射速": 700, "后坐力": 45, "机动性": 60},
        "适合": "均衡型，中距离",
        "改装思路": {
            "高dpi快反应": ("轻型枪托 + 红点瞄具 + 战术握把", "精校：开镜速度+15%，腰射精度+10%"),
            "低dpi慢反应": ("重型枪管 + 4倍镜 + 垂直握把", "精校：后坐力控制+20%，开镜稳定+15%"),
            "默认": ("消音器 + 全息镜 + 直角握把", "精校：后坐力-10%，机动+5%")
        }
    },
    "MP5": {
        "type": "冲锋枪",
        "base_stats": {"伤害": 28, "射速": 800, "后坐力": 35, "机动性": 80},
        "适合": "近战高速，高机动",
        "改装思路": {
            "高dpi快反应": ("无枪托 + 反射式瞄具 + 镭射指示器", "精校：腰射精度+20%，跑射速度+15%"),
            "低dpi慢反应": ("战术护木 + 全息镜 + 消焰器", "精校：开镜速度+10%，水平后坐-15%"),
            "默认": ("扩容弹匣 + 反射式瞄具 + 战术握把", "精校：弹容量+10，换弹速度+10%")
        }
    },
    "AK-47": {
        "type": "突击步枪",
        "base_stats": {"伤害": 42, "射速": 600, "后坐力": 70, "机动性": 45},
        "适合": "高伤害，后坐力大",
        "改装思路": {
            "高dpi快反应": ("短枪管 + 红点 + 轻型护木", "精校：开镜速度+20%，垂直后坐-10%"),
            "低dpi慢反应": ("补偿器 + 4倍镜 + 垂直握把", "精校：后坐力-25%，屏息时间+30%"),
            "默认": ("制退器 + 全息镜 + 战术握把", "精校：后坐力-15%，开镜稳定+10%")
        }
    },
    "AWM": {
        "type": "狙击步枪",
        "base_stats": {"伤害": 95, "射速": 40, "后坐力": 90, "机动性": 20},
        "适合": "一击致命，极低容错",
        "改装思路": {
            "高dpi快反应": ("快速拉栓 + 8倍镜 + 轻量化枪托", "精校：开镜速度+25%，拉栓速度+15%"),
            "低dpi慢反应": ("双脚架 + 15倍镜 + 消音器", "精校：屏息晃动-30%，子弹下坠-20%"),
            "默认": ("7倍镜 + 消音器 + 直拉枪栓", "精校：开镜速度+15%，伤害距离+10%")
        }
    }
}

# ==================== 改枪码生成 ====================
def generate_weapon_code():
    """生成8位随机分享码（模拟游戏格式）"""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=8))

# ==================== 主界面类 ====================
class WeaponAdvisor:
    def __init__(self, root):
        self.root = root
        self.root.title("三角洲行动 - 枪械私人顾问")
        self.root.geometry("520x700")
        self.root.resizable(False, False)

        self.dpi = tk.IntVar(value=800)
        self.reaction_time = tk.DoubleVar(value=250.0)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="三角洲行动 · 专属枪械推荐", font=("微软雅黑", 16, "bold")).pack(pady=10)

        # DPI 测试区
        dpi_frame = ttk.LabelFrame(self.root, text="① 鼠标 DPI 测试", padding=10)
        dpi_frame.pack(fill="x", padx=20, pady=5)

        ttk.Label(dpi_frame, text="请将鼠标放在起点，按住左键水平移动 10 cm 后松开").pack()
        self.dpi_canvas = tk.Canvas(dpi_frame, height=30, bg="lightgray")
        self.dpi_canvas.pack(fill="x", pady=5)
        self.dpi_canvas.bind("<Button-1>", self.start_dpi_test)
        self.dpi_canvas.bind("<B1-Motion>", self.update_dpi_test)
        self.dpi_canvas.bind("<ButtonRelease-1>", self.end_dpi_test)
        self.dpi_testing = False
        self.dpi_start_x = 0
        self.dpi_pixel_moved = 0

        ttk.Label(dpi_frame, text="当前测得 DPI：").pack(side="left")
        ttk.Label(dpi_frame, textvariable=self.dpi, foreground="red").pack(side="left")
        ttk.Button(dpi_frame, text="手动输入", command=self.manual_dpi).pack(side="right")

        # 反应时间测试区
        rt_frame = ttk.LabelFrame(self.root, text="② 反应速度测试", padding=10)
        rt_frame.pack(fill="x", padx=20, pady=5)

        self.rt_label = ttk.Label(rt_frame, text="点击下方开始测试（共5次）", font=("微软雅黑", 10))
        self.rt_label.pack()
        self.rt_button = tk.Button(rt_frame, text="开始反应测试", bg="gray", font=("微软雅黑", 12, "bold"),
                                   command=self.start_reaction_test, state="normal")
        self.rt_button.pack(pady=5, ipadx=20)
        ttk.Label(rt_frame, text="平均反应时间(ms)：").pack(side="left")
        ttk.Label(rt_frame, textvariable=self.reaction_time, foreground="red").pack(side="left")

        # 分析按钮
        ttk.Button(self.root, text="🔍 开始分析并生成方案", command=self.analyze).pack(pady=15)

        # 结果显示区
        result_frame = ttk.LabelFrame(self.root, text="🎯 推荐方案", padding=10)
        result_frame.pack(fill="both", expand=True, padx=20, pady=5)

        self.result_text = tk.Text(result_frame, height=15, width=55, font=("微软雅黑", 10), wrap="word")
        self.result_text.pack()

        self.code_label = ttk.Label(self.root, text="改枪码：-----------", font=("微软雅黑", 12, "bold"), foreground="blue")
        self.code_label.pack(pady=5)

    # ---------- DPI 测试逻辑 ----------
    def start_dpi_test(self, event):
        self.dpi_testing = True
        self.dpi_start_x = event.x
        self.dpi_pixel_moved = 0

    def update_dpi_test(self, event):
        if self.dpi_testing:
            self.dpi_pixel_moved = abs(event.x - self.dpi_start_x)

    def end_dpi_test(self, event):
        if self.dpi_testing:
            self.dpi_testing = False
            physical_inch = 3.937
            if self.dpi_pixel_moved > 0:
                calc_dpi = int(self.dpi_pixel_moved / physical_inch)
                self.dpi.set(max(100, min(12000, calc_dpi)))
                messagebox.showinfo("DPI 测试", f"移动像素：{self.dpi_pixel_moved}\n计算 DPI：{self.dpi.get()}")
            else:
                messagebox.showwarning("注意", "没有检测到移动，请再试一次")

    def manual_dpi(self):
        win = tk.Toplevel(self.root)
        win.title("手动输入 DPI")
        ttk.Label(win, text="请输入鼠标 DPI：").pack(padx=20, pady=10)
        entry = ttk.Entry(win)
        entry.pack(padx=20)
        def set_dpi():
            try:
                val = int(entry.get())
                if 100 <= val <= 12000:
                    self.dpi.set(val)
                    win.destroy()
                else:
                    messagebox.showwarning("错误", "DPI 范围 100-12000")
            except:
                messagebox.showwarning("错误", "请输入整数")
        ttk.Button(win, text="确定", command=set_dpi).pack(pady=10)

    # ---------- 反应测试逻辑 ----------
    def start_reaction_test(self):
        self.rt_button.config(state="disabled", text="等待绿色...")
        self.root.update()
        delay = random.randint(1000, 3000)
        self.root.after(delay, self.show_green)

    def show_green(self):
        self.rt_button.config(bg="green", text="点击！！！", state="normal")
        self.rt_start_time = time.time()
        self.rt_button.config(command=self.record_reaction)

    def record_reaction(self):
        reaction = (time.time() - self.rt_start_time) * 1000
        if not hasattr(self, 'reaction_times'):
            self.reaction_times = []
        self.reaction_times.append(reaction)
        self.rt_button.config(bg="gray", text="继续测试", command=self.start_reaction_test)

        if len(self.reaction_times) >= 5:
            avg = sum(self.reaction_times) / len(self.reaction_times)
            self.reaction_time.set(round(avg, 1))
            self.rt_button.config(bg="lightgray", text="测试完成", state="disabled", command=None)
            messagebox.showinfo("反应测试", f"5次平均：{avg:.1f} ms")
            self.reaction_times = []
        else:
            self.rt_button.config(text=f"第{len(self.reaction_times)}次完成，点击继续")

    # ---------- 分析与推荐 ----------
    def analyze(self):
        dpi_val = self.dpi.get()
        rt_val = self.reaction_time.get()

        if dpi_val >= 800:
            dpi_cat = "高dpi"
        else:
            dpi_cat = "低dpi"

        if rt_val <= 200:
            rt_cat = "快反应"
        else:
            rt_cat = "慢反应"

        combo = f"{dpi_cat}{rt_cat}"

        if "高dpi快" in combo:
            weapon_key = "MP5"
        elif "低dpi慢" in combo:
            weapon_key = "AWM"
        elif "高dpi慢" in combo:
            weapon_key = "M4A1"
        else:
            weapon_key = "AK-47"

        weapon = WEAPON_DB[weapon_key]
        if combo in weapon["改装思路"]:
            mod, tune = weapon["改装思路"][combo]
        else:
            mod, tune = weapon["改装思路"]["默认"]

        code = generate_weapon_code()

        result = f"""【用户画像】
鼠标 DPI：{dpi_val}  |  平均反应时间：{rt_val} ms
类别：{combo}

【推荐枪械】
{weapon_key} （{weapon['type']}）
特点：{weapon['适合']}

【改装方案】
{mod}

【精校参数】
{tune}

【改枪码】
{code}
（可在游戏内“导入方案”中使用）
"""
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        self.code_label.config(text=f"改枪码：{code}")

# ==================== 启动 ====================
if __name__ == "__main__":
    root = tk.Tk()
    app = WeaponAdvisor(root)
    root.mainloop()
