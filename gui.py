import tkinter as tk
from tkinter import filedialog, messagebox
from hasher import get_hash
from storage import store_record, get_record
from utils import log, export_report

rows=[]
BG='#FDEEF4'; PANEL='#FFF8FB'; ACCENT='#E8B4C8'; BTN='#CDEAC0'; TEXT='#5B4B56'

root=tk.Tk(); root.title('File Integrity Checker'); root.geometry('620x520'); root.configure(bg=BG)

# Title bar
bar=tk.Frame(root,bg=ACCENT,height=40)
bar.pack(fill='x',padx=12,pady=(12,0))
for c in ['#FF8FAB','#F9C74F','#90BE6D']:
    tk.Label(bar,text='  ',bg=c).pack(side='left',padx=4,pady=10)
tk.Label(bar,text='  File Integrity Checker  ',bg=ACCENT,fg=TEXT,font=('Arial',14,'bold')).pack(side='left',padx=10)

main=tk.Frame(root,bg=PANEL,bd=2,relief='ridge')
main.pack(fill='both',expand=True,padx=12,pady=(0,12))

status=tk.Label(main,text='Ready ✿',bg=PANEL,fg=TEXT,font=('Arial',12,'bold'))
status.pack(pady=18)

card=tk.Frame(main,bg=BG)
card.pack(pady=10,padx=20,fill='x')


def hover(btn,on=True):
    btn.config(bg=ACCENT if on else BTN)

def nice_button(parent,text,cmd):
    b=tk.Button(parent,text=text,command=cmd,bg=BTN,fg=TEXT,font=('Arial',12,'bold'),width=22,height=2,bd=0,activebackground=ACCENT,cursor='hand2')
    b.bind('<Enter>',lambda e:hover(b,True))
    b.bind('<Leave>',lambda e:hover(b,False))
    return b

def store():
    path=filedialog.askopenfilename()
    if not path:return
    h,t=get_hash(path)
    store_record(path,'sha256',h)
    rows.append([path,'STORED',round(t,4)])
    log(f'Stored {path}')
    status.config(text='Hash Stored ✓',fg='#2D6A4F')
    messagebox.showinfo('Success','Hash Stored Successfully')

def verify():
    path=filedialog.askopenfilename()
    if not path:return
    rec=get_record(path)
    if not rec:
        messagebox.showwarning('Warning','No record found')
        return
    h,t=get_hash(path,rec['algo'])
    ok=h==rec['hash']
    msg='File is SAFE ✓' if ok else 'File is MODIFIED ✗'
    status.config(text=msg,fg='#2D6A4F' if ok else '#B00020')
    rows.append([path,'SAFE' if ok else 'MODIFIED',round(t,4)])
    messagebox.showinfo('Result',msg) if ok else messagebox.showerror('Result',msg)

def report():
    export_report(rows)
    messagebox.showinfo('Report','Report Exported Successfully')

for txt,cmd in [('Store File Hash 📁',store),('Verify File 🔍',verify),('Export Report 📝',report),('Exit 🌸',root.destroy)]:
    nice_button(card,txt,cmd).pack(pady=8)

footer=tk.Label(main,text='Cyber Security PBL',bg=PANEL,fg=TEXT,font=('Arial',10))
footer.pack(side='bottom',pady=14)

root.mainloop()
