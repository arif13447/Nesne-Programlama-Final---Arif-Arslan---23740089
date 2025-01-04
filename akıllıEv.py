from abc import ABC, abstractmethod

class Controllable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def is_on(self):
        pass

class Appliance(Controllable):
    def __init__(self):
        self._is_on = False

    def turn_on(self):
        self._is_on = True
        print(f"{self.__class__.__name__} açıldı.")

    def turn_off(self):
        self._is_on = False
        print(f"{self.__class__.__name__} kapatıldı.")

    def is_on(self):
        return self._is_on

class Light(Appliance):
    def __init__(self, brightness=100):
        super().__init__()
        self.brightness = brightness

    def set_brightness(self, brightness):
        self.brightness = brightness
        print(f"Işık parlaklığı {brightness} olarak ayarlandı.")

class Thermostat(Appliance):
    def __init__(self, temperature=22):
        super().__init__()
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Sıcaklık {temperature}°C olarak ayarlandı.")

class SecuritySystem(Appliance):
    def __init__(self):
        super().__init__()
        self.alarm_triggered = False

    def trigger_alarm(self):
        self.alarm_triggered = True
        print("Alarm tetiklendi!")

    def reset_alarm(self):
        self.alarm_triggered = False
        print("Alarm sıfırlandı.")

def main():
    light = Light()
    thermostat = Thermostat()
    security_system = SecuritySystem()

    while True:
        print("\n--- Akıllı Ev Yönetim Sistemi ---")
        print("1. Işığı aç")
        print("2. Işığı kapat")
        print("3. Işık durumunu sorgula")
        print("4. Işık parlaklığını ayarla")
        print("5. Sıcaklığı ayarla")
        print("6. Güvenlik sistemini aç")
        print("7. Güvenlik sistemini kapat")
        print("8. Alarmı tetikle")
        print("9. Alarmı sıfırla")
        print("10. Çıkış")
        
        choice = input("Seçiminizi yapın: ")

        if choice == '1':
            light.turn_on()
        elif choice == '2':
            light.turn_off()
        elif choice == '3':
            print(f"Işık durumu: {'Açık' if light.is_on() else 'Kapalı'}")
        elif choice == '4':
            brightness = int(input("Yeni parlaklık değerini girin (0-100): "))
            light.set_brightness(brightness)
        elif choice == '5':
            temp = int(input("Yeni sıcaklık değerini girin: "))
            thermostat.set_temperature(temp)
        elif choice == '6':
            security_system.turn_on()
        elif choice == '7':
            security_system.turn_off()
        elif choice == '8':
            security_system.trigger_alarm()
        elif choice == '9':
            security_system.reset_alarm()
        elif choice == '10':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()