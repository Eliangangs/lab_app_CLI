import sys
import subprocess
import os

def list_labs():
    """Виводить список доступних лабораторних робіт."""
    labs_dir = "labs"
    if not os.path.exists(labs_dir):
        print("Папка 'labs' не знайдена.")
        return

    labs = [d for d in os.listdir(labs_dir) if os.path.isdir(os.path.join(labs_dir, d)) and d.startswith("lab")]
    if not labs:
        print("Не знайдено жодної лабораторної роботи.")
        return
    print("Доступні лабораторні роботи:")
    for i, lab in enumerate(labs):
        readme_path = os.path.join(labs_dir, lab, "README.md")
        description = ""
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                 try:
                     description = f.readline().strip().replace("# Лабораторна робота", "").strip()
                 except Exception as e:
                      print(f"Помилка читання опису лаби: {e}")
        print(f"{i + 1}. {lab} - {description if description else 'Без опису'}")


def run_lab(lab_number):
    """Запускає обрану лабораторну роботу."""
    labs_dir = "labs"
    lab_dir = os.path.join(labs_dir, f"lab{lab_number}")
    lab_file = os.path.join(lab_dir, f"lab{lab_number}.py")

    if not os.path.exists(lab_dir) or not os.path.exists(lab_file):
        print(f"Лабораторна робота {lab_number} не знайдена.")
        return

    try:
        print(f"Запуск лабораторної роботи {lab_number}...")
        subprocess.run(["streamlit", "run", lab_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Помилка запуску лабораторної: {e}")
    except FileNotFoundError:
       print("Streamlit не встановлено. Запустіть 'pip install streamlit'")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python cli.py <list|run> <lab_number>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        list_labs()
    elif command == "run":
        if len(sys.argv) < 3:
            print("Використання: python cli.py run <lab_number>")
            sys.exit(1)
        try:
           lab_number = int(sys.argv[2])
           run_lab(lab_number)
        except ValueError:
            print("Номер лабораторної має бути цілим числом")
    else:
        print("Невідома команда. Використовуйте 'list' або 'run'.")

if __name__ == '__main__':
    run_lab()