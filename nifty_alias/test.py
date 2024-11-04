import subprocess
from rich.console import Console
from rich.panel import Panel

# Rich konsolu oluştur
console = Console()


def run_command(command):
    try:
        # Komutu çalıştır
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout.strip()
        error = result.stderr.strip()

        return output, error
    except Exception as e:
        return None, str(e)


def display_output(command, output, error):
    # Komut kutusu
    command_panel = Panel(
        f"[bold cyan]Command:[/bold cyan] {command}",
        title="Executed Command",
        title_align="left",
    )

    # Çıktı kutusu
    if output:
        output_panel = Panel(output, title="Output", title_align="left", style="green")
    else:
        output_panel = Panel(
            "No output", title="Output", title_align="left", style="yellow"
        )

    # Hata kutusu
    if error:
        error_panel = Panel(error, title="Error", title_align="left", style="red")
    else:
        error_panel = Panel(
            "No errors", title="Error", title_align="left", style="yellow"
        )

    # Sonuçları konsolda göster
    console.print(command_panel)
    console.print(output_panel)
    console.print(error_panel)


if __name__ == "__main__":
    # Kullanıcıdan komut al
    command = "curl ifconfig.me"

    # Komutu çalıştır
    output, error = run_command(command)

    # Sonuçları göster
    display_output(command, output, error)
