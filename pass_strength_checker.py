import re
import sys
import time
from rich.console import Console
from rich.progress import track
from rich.text import Text

console = Console()

# Neon typing effect
def type_effect(text, style="bold magenta", delay=0.03):
    for char in text:
        console.print(char, style=style, end="")
        sys.stdout.flush()
        time.sleep(delay)
    console.print("")

# Banner
def banner():
    neon_banner = r"""
  ____  _   _ ____  _____   _     ___   ____ _  __
 / ___|| | | |  _ \| ____| | |   / _ \ / ___| |/ /
 \___ \| | | | |_) |  _|   | |  | | | | |   | ' / 
  ___) | |_| |  __/| |___  | |__| |_| | |___| . \ 
 |____/ \___/|_|   |_____| |_____\___/ \____|_|\_\
                                                  
    """
    console.print(Text(neon_banner, style="bold bright_green"))
    type_effect("               Password Strength Checker \n", "bold bright_green", 0.02)

# Password strength check
def pass_check(password):
    score = 0
    tips = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Enter at least 8+ characters (12+ is better).")

    # Character variety
    checks = {
        "lowercase": r"[a-z]",
        "uppercase": r"[A-Z]",
        "digit": r"\d",
        "symbol": r"[^\w\s]"
    }

    for label, pattern in checks.items():
        if re.search(pattern, password):
            score += 1
        else:
            tips.append(f"Add at least one {label}.")

    # Repetition check
    if re.search(r"(.)\1{2,}", password):
        tips.append("Avoid repeating the same character 3+ times.")

    # Verdict
    verdict = "Strong" if score >= 5 else ("Moderate" if score >= 3 else "Weak")
    return verdict, score, tips


if __name__ == "__main__":
    
    type_effect("\n Initializing SUPE LOCK...\n", "bold green")
    banner()

    for step in track(range(20), description=" Loading security modules..."):
        time.sleep(0.05)

    console.print("\n[bold blue]Enter your password:[/bold blue] ", end="")
    pwd = input()

    verdict, score, tips = pass_check(pwd)

    # Neon verdict colors
    neon_colors = {
        "Strong": "bold bright_green",
        "Moderate": "bold yellow",
        "Weak": "bold bright_red"
    }

    glow_text = Text(f"\nVerdict: {verdict} (Score {score})", style=neon_colors[verdict])
    console.print(glow_text)

    # Show improvement tips
    if tips:
        console.print("\n[bold cyan]Improve by:[/bold cyan]")
        for t in tips:
            console.print(f"[bold green]- {t}[/bold green]")
    
    input("\nPress Enter to exit...")

