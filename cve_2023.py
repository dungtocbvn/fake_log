import time
import sys
import random

def fake_exploit_logs(duration=15):
    logs = [
        "[*] Đang dò phiên bản dịch vụ...",
        "[*] Phát hiện cổng mở: 4444",
        "[*] Đang gửi payload...",
        "[*] Bypass xác thực...",
        "[*] Tải shellcode...",
        "[*] Thiết lập kết nối reverse shell...",
        "[*] Thành công! Đang mở phiên..."
    ]
    total_steps = 100
    delay = duration / total_steps
    for i in range(total_steps + 1):
        bar = "#" * (i // 2)
        spaces = " " * ((100 - i) // 2)
        sys.stdout.write(f"\r[{bar}{spaces}] {i}%")
        sys.stdout.flush()
        if i in [10, 30, 50, 70, 90, 100]:
            print("\n" + random.choice(logs))
        time.sleep(delay)
    print("\n[+] Giả lập exploit hoàn tất!")

def fake_shell():
    responses = {
        "whoami": "nt authority\\system",
        "ipconfig": (
            "Windows IP Configuration\n\n"
            "Ethernet adapter Ethernet0:\n"
            "   Connection-specific DNS Suffix  . : localdomain\n"
            "   IPv4 Address. . . . . . . . . . . : 192.168.1.10\n"
            "   Subnet Mask . . . . . . . . . . . : 255.255.255.0\n"
            "   Default Gateway . . . . . . . . . : 192.168.1.1"
        ),
        "dir": (
            " Volume in drive C has no label.\n"
            " Volume Serial Number is 1234-ABCD\n\n"
            " Directory of C:\\Users\\Administrator\n\n"
            "09/09/2025  10:00 AM    <DIR>          .\n"
            "09/09/2025  10:00 AM    <DIR>          ..\n"
            "08/20/2025  05:12 PM             1,024 secret.docx\n"
            "08/22/2025  07:45 PM    <DIR>          Desktop\n"
            "               1 File(s)          1,024 bytes\n"
            "               2 Dir(s)  20,000,000,000 bytes free"
        ),
        "hostname": "WIN-SERVER2019",
        "systeminfo": (
            "Host Name:                 WIN-SERVER2019\n"
            "OS Name:                   Microsoft Windows Server 2019 Datacenter\n"
            "OS Version:                10.0.17763 N/A Build 17763\n"
            "System Manufacturer:       VMware, Inc.\n"
            "System Model:              VMware Virtual Platform\n"
            "System Type:               x64-based PC"
        ),
    }

    print("\n[+] Đã có shell trên mục tiêu (giả lập). Gõ lệnh hoặc 'exit' để thoát.\n")
    while True:
        cmd = input("C:\\Windows\\System32> ").strip().lower()
        if cmd in ["exit", "quit"]:
            print("[+] Đóng phiên shell.")
            break
        output = responses.get(cmd, f"'{cmd}' is not recognized as an internal or external command,\noperable program or batch file.")
        print(output)

if __name__ == "__main__":
    print("=== DEMO KALI (FAKE EXPLOIT + SHELL) ===")
    print("[*] Đang khai thác lỗ hổng (mô phỏng)...")
    fake_exploit_logs(15)
    fake_shell()
