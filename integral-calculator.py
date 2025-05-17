import tkinter as tk
from tkinter import messagebox
from sympy import symbols, integrate, sympify, oo, pi, E

def calculate_integral():
    var = symbols('x')
    expression = entry_expression.get()
    
    if integral_type.get() == "definite":
        lower_text = entry_lower.get()
        upper_text = entry_upper.get()
        
        # 处理积分限（支持 pi 和无穷）
        def parse_limit(text):
            if text == "+":
                return oo
            elif text == "-":
                return -oo
            elif text.lower() == "pi":  # 处理 pi和自然对数e
                return pi
            elif text == "E":
                return E
            else:
                try:
                    return float(text)
                except:
                    messagebox.showerror("错误", f"输入无效: {text}")
                    raise ValueError("无效输入")

        try:
            lower_limit = parse_limit(lower_text)
            upper_limit = parse_limit(upper_text)
        except:
            return  # 输入无效，直接返回
        
        try:
            expr = sympify(expression)
            result = integrate(expr, (var, lower_limit, upper_limit))
            messagebox.showinfo("计算结果", f"定积分结果为：{result}")
        except Exception as e:
            messagebox.showerror("错误", f"输入无效: {e}")
    else:
        try:
            expr = sympify(expression)
            result = integrate(expr, var)
            messagebox.showinfo("计算结果", f"不定积分结果为：{result} + C")
        except Exception as e:
            messagebox.showerror("错误", f"输入无效: {e}")

def show_special_rules():
    rules = "特殊输入规则：\n\n" \
            "• 使用'x'作为积分变量\n" \
            "• 乘号使用'*'，如2*x和2*sin(x)\n" \
            "• 次方使用'**'（例如：x**2表示x²）\n" \
            "• 除号使用'/'\n" \
            "• 圆周率用'pi'表示\n" \
            "• 自然对数e用'E'表示\n" \
            "• 三角函数直接使用sin、cos、tan等，其表达式用括号括起来\n" \
            "  例如：sin(x)和sin(2*x+1)\n" \
            "• 反三角函数如arcsin、arccos、arctan等无法使用该程序求解\n" \
            "• 自然对数函数：log(x)（e为底）\n" \
            "• 以a为底n的对数表示为'log(n, a)'\n" \
            "• 定积分的上下限如果是正无穷或负无穷，直接输入+或-\n" \
            "• Abs(x)表示x的绝对值\n" \
            "• exp(x)表示自然对数e的x次幂"
    messagebox.showinfo("输入规则说明", rules)

def update_ui():
    if integral_type.get() == "definite":
        lower_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entry_lower.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        upper_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        entry_upper.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    else:
        lower_label.grid_forget()
        entry_lower.grid_forget()
        upper_label.grid_forget()
        entry_upper.grid_forget()

app = tk.Tk()
app.title("积分计算器")
app.geometry("400x350")
app.resizable(False, False)

# 使用网格布局来组织UI元素
frame = tk.Frame(app, padx=20, pady=20)
frame.pack(fill="both", expand=True)

integral_type = tk.StringVar(value="indefinite")

# 第一行：标题
title_label = tk.Label(frame, text="积分计算器", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=1, columnspan=2, pady=10)

# 第二行：选择积分类型
type_frame = tk.Frame(frame)
type_frame.grid(row=1, column=0, columnspan=2, pady=10)
tk.Label(type_frame, text="选择积分类型:").pack(side="left", padx=5)
tk.Radiobutton(type_frame, text="定积分", variable=integral_type, value="definite", 
               command=update_ui).pack(side="left", padx=5)
tk.Radiobutton(type_frame, text="不定积分", variable=integral_type, value="indefinite", 
               command=update_ui).pack(side="left", padx=5)

# 定义积分的上下限和表达式输入框
lower_label = tk.Label(frame, text="下限:")
entry_lower = tk.Entry(frame, width=15)
upper_label = tk.Label(frame, text="上限:")
entry_upper = tk.Entry(frame, width=15)

# 表达式输入行
expr_label = tk.Label(frame, text="表达式:")
expr_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_expression = tk.Entry(frame, width=30)
entry_expression.grid(row=4, column=1, padx=5, pady=5, sticky="w")

# 按钮区域
button_frame = tk.Frame(frame)
button_frame.grid(row=5, column=0, columnspan=2, pady=15)
tk.Button(button_frame, text="计算", command=calculate_integral, width=10).pack(side="left", padx=10)
tk.Button(button_frame, text="输入规则", command=show_special_rules, width=10).pack(side="left", padx=10)

# 初始化UI状态
update_ui()

app.mainloop()
