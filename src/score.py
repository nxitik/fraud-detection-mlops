THRESHOLD = 0.5

def is_fraud(score: float) -> bool:
    return score >= THRESHOLD

if __name__ == "__main__":
    print(is_fraud(0.7))
