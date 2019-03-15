def bonus(spent, current):
    golden = 100
    silver = 70
    blue = 50
    total_spent = spent + current
    if 1 < total_spent < 15_001:
        status = blue
    if 15_001 < total_spent <= 150_000:
        status = silver
    if total_spent > 150_000:
        status = golden
    return current // 1000 * status


