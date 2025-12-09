from core.controller import CentralController
from core.factories.device_factory import DeviceFactory
from core.builders.report_builder import ReportBuilder


def test_singleton():
    c1 = CentralController()
    c2 = CentralController()
    assert c1 is c2, "Singleton buzilgan!"

def test_device_factory():
    factory = DeviceFactory()
    light = factory.create("street_light")
    assert light is not None, "Factory device yaratmadi!"

def test_report_builder():
    builder = ReportBuilder()
    builder.header("Test Report")
    report = builder.build()
    assert "Test Report" in report, "Report builder noto‘g‘ri ishlayapti!"


def run_all_tests():
    print("Success")

    test_singleton()
    print("✔ Singleton OK")

    test_device_factory()
    print("✔ Factory OK")

    test_report_builder()
    print("✔ Report Builder OK")

    test_proxy_access()
    print("✔ Proxy Access OK")

    print("\n=== BARCHA TESTLAR MUVAFFAQIYATLI O'TDI ===")


if __name__ == "__main__":
    run_all_tests()

