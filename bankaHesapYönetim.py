class Account:
    accounts = []  

    def __init__(self, account_number, owner, balance):
        self.__account_number = account_number  
        self.__owner = owner 
        self.__balance = balance  
        Account.accounts.append(self)  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} TL yatırıldı. Yeni bakiye: {self.__balance} TL")
            Bank.track_transaction(f"Yatırma: {amount} TL, Hesap No: {self.__account_number}")
        else:
            print("Yatırılacak miktar sıfırdan büyük olmalıdır.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} TL çekildi. Yeni bakiye: {self.__balance} TL")
            Bank.track_transaction(f"Çekme: {amount} TL, Hesap No: {self.__account_number}")
        elif amount > self.__balance:
            print("Yetersiz bakiye.")
        else:
            print("Çekilecek miktar sıfırdan büyük olmalıdır.")

    def view_balance(self):
        print(f"Hesap Sahibi: {self.__owner}")
        print(f"Hesap Numarası: {self.__account_number}")
        print(f"Bakiye: {self.__balance} TL")


class Bank:
    transaction_history = []  

    @staticmethod
    def display_bank_info():
        print("Banka Hesap Yönetim Sistemi")
        print("Tüm işlemler kaydedilmektedir.")

    @staticmethod
    def track_transaction(description):
        Bank.transaction_history.append(description)

    @staticmethod
    def display_transaction_history():
        print("İşlem Geçmişi:")
        for transaction in Bank.transaction_history:
            print(transaction)


def main():
    Bank.display_bank_info()

    while True:
        print("\n1. Hesap Oluştur")
        print("2. Para Yatır")
        print("3. Para Çek")
        print("4. Bakiye Görüntüle")
        print("5. İşlem Geçmişini Görüntüle")
        print("6. Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == '1':
            account_number = input("Hesap Numarası: ")
            owner = input("Hesap Sahibi: ")
            balance = float(input("Başlangıç Bakiyesi: "))
            Account(account_number, owner, balance)
            print("Hesap oluşturuldu.")

        elif choice == '2':
            account_number = input("Hesap Numarası: ")
            account_to_deposit = next((acc for acc in Account.accounts if acc._Account__account_number == account_number), None)
            if account_to_deposit:
                amount = float(input("Yatırılacak Miktar: "))
                account_to_deposit.deposit(amount)
            else:
                print("Hesap bulunamadı.")

        elif choice == '3':
            account_number = input("Hesap Numarası: ")
            account_to_withdraw = next((acc for acc in Account.accounts if acc._Account__account_number == account_number), None)
            if account_to_withdraw:
                amount = float(input("Çekilecek Miktar: "))
                account_to_withdraw.withdraw(amount)
            else:
                print("Hesap bulunamadı.")

        elif choice == '4':
            account_number = input("Hesap Numarası: ")
            account_to_view = next((acc for acc in Account.accounts if acc._Account__account_number == account_number), None)
            if account_to_view:
                account_to_view.view_balance()
            else:
                print("Hesap bulunamadı.")

        elif choice == '5':
            Bank.display_transaction_history()

        elif choice == '6':
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()