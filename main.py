# Kalkulatori i Shpenzimeve Mujore
def get_user_data():
    """Merr të ardhurat dhe shpenzimet mujore nga përdoruesi."""
    print("👋 Mirë se vini në Kalkulatorin e Shpenzimeve Mujore!\n")

    # emri i përdoruesit
    name = input("Shkruaj emrin tënd: ").strip()
    while not name:
        name = input("Emri nuk mund të jetë bosh. Provo përsëri: ").strip()

    # Merr të ardhurat
    while True:
        try:
            income = float(input("Shkruaj të ardhurat mujore (€): "))
            if income >= 0:
                break
            else:
                print("Të ardhurat nuk mund të jenë negative.")
        except ValueError:
            print("Ju lutem shkruani një numër të vlefshëm.")

    # Merr shpenzimet sipas kategorive
    print("\nTani shkruaj shpenzimet për secilën kategori.")
    categories = ["Qira", "Ushqim", "Transport", "Internet", "Tjera"]
    expenses = {}

    for category in categories:
        while True:
            try:
                amount = float(input(f"{category}: €"))
                if amount >= 0:
                    expenses[category] = amount
                    break
                else:
                    print("Shuma nuk mund të jetë negative.")
            except ValueError:
                print("Ju lutem shkruani një numër të vlefshëm.")

    return {
        "name": name,
        "income": income,
        "expenses": expenses
    }


def calculate_total_expenses(expenses):
    """Kthen totalin e shpenzimeve mujore."""
    return sum(expenses.values())


def calculate_balance(income, total_expenses):
    """Llogarit bilancin e mbetur."""
    return income - total_expenses


def show_summary(user_data, total_expenses, balance):
    """Shfaq përmbledhje të shpenzimeve dhe një mesazh."""
    print("\n📊 --- PËRMBLEDHJE ---")
    print(f"Emri: {user_data['name']}")
    print(f"Të ardhurat mujore: €{user_data['income']:.2f}")
    print(f"Totali i shpenzimeve: €{total_expenses:.2f}")
    print(f"Bilanci i mbetur: €{balance:.2f}")

    if balance > 100:
        print("💡 Po kursen mirë! Vazhdo kështu.")
    elif 0 <= balance <= 100:
        print("⚠️ Duhet të kujdesesh për shpenzimet.")
    else:
        print("❗ Po shpenzon më shumë se të ardhurat. Konsidero të reduktosh shpenzimet.")

    # Opsionale: kategoria me shpenzimin më të madh
    biggest_category = max(user_data['expenses'], key=user_data['expenses'].get)
    print(f"\n📌 Shpenzimi më i madh ishte për: {biggest_category} (€{user_data['expenses'][biggest_category]:.2f})")


# Rrjedha kryesore
if __name__ == "__main__":
    user_info = get_user_data()
    total = calculate_total_expenses(user_info['expenses'])
    balance = calculate_balance(user_info['income'], total)
    show_summary(user_info, total, balance)