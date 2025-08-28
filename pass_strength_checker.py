import re
import sys
import time
from rich.console import Console
from rich.progress import track
from rich.text import Text

console = Console()

def type_effect(text, style="bold magenta", delay=0.03):
    """Typing effect with neon-style colors"""
    for char in text:
        console.print(char, style=style, end="")
        sys.stdout.flush()
        time.sleep(delay)
    console.print("")  

def pass_check(password):
    score = 0
    tips = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Enter at least 8+ characters (12+ is better).")

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

    if re.search(r"(.)\1{2,}", password):
        tips.append("Avoid repeating the characters 3+ times.")

    verdict = "Strong" if score >= 5 else ("Moderate" if score >= 3 else "Weak")
    return verdict, score, tips

if __name__ == "__main__":
    type_effect(" Initializing Password Strength Checker...\n", "bold green")
    
    for step in track(range(20), description=" Loading modules..."):
        time.sleep(0.05)

    console.print("\n[bold blue]Enter your password:[/bold blue] ", end="")
    pwd = input()
    
    verdict, score, tips = pass_check(pwd)

    neon_colors = {
        "Strong": "bold bright_green",
        "Moderate": "bold yellow",
        "Weak": "bold bright_red"
    }

    glow_text = Text(f"\nVerdict: {verdict} (Score {score})", style=neon_colors[verdict])
    console.print(glow_text)

    if tips:
        console.print("\n[bold cyan]Improve by:[/bold cyan]")
        for t in tips:
            console.print(f"[bold green]- {t}[/bold green]")
