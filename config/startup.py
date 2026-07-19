import subprocess, sys

def install_all():
    print("⏳ Installing strictly pinned architecture packages onto Colab's native stack (~30s)...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-q",
        "timm==0.9.12", "peft==0.6.2", "captum==0.7.0", "lime==0.2.0.1", "pydicom==2.4.3"
    ])
    print("✅ Packages ready! Using native modern PyTorch and NumPy.")

install_all()
