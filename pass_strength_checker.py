import re

def pass_check(password):
    score = 0
    tips = []

    if len(password)>=12:
        score+=2
    elif len(password)>=8:
        score+=1
    else:
        tips.append("Enter at least 8+ characters (12+ is better).")

    checks ={
        "lowercase": r"[a-z]",
        "uppercase": r"[A-Z]",
        "digit": r"\d",
        "symbol": r"[^\w\s]"
    }

    for label, pattern in checks.items():
        if re.search(pattern, password):
            score+=1
        else:
            tips.append(f"Add at least one {label}.")

    if re.search(r"(.)\1{2,}", password):
        tips.append("Avoid repeating the characters 3+ times.")

    verdict= "Strong" if score>=5 else ("Moderate" if score>=3 else "Weak")

    return verdict, score, tips

if __name__ == "__main__":
    pwd= input("Enter a password: ")
    verdict, score, tips= pass_check(pwd)
    print(f"Verdict: {verdict} (Score {score})")

    if tips:
        print("Improve by: ")
        for t in tips:
            print("-",t)