from datetime import datetime
import csv, os

def log(msg):
    with open('activity.log','a') as f:
        f.write(f'{datetime.now()} - {msg}\n')

def export_report(rows):
    os.makedirs('reports', exist_ok=True)
    with open('reports/report.csv','w',newline='') as f:
        w=csv.writer(f)
        w.writerow(['File','Status','Time'])
        w.writerows(rows)