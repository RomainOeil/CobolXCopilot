import pytest
from main import main
from operations import operations
from data import read_balance, write_balance

@pytest.fixture(autouse=True)
def reset_balance():
    """
    Fixture to reset the balance before each test.
    """
    write_balance(1000.00)  # Reset balance to 1000.00 before each test

def test_view_balance(capsys):
    """
    Test Case TC-1.1: View Current Balance
    """
    operations("TOTAL")
    captured = capsys.readouterr()
    assert "Current Balance: 1000.00" in captured.out

def test_credit_valid_amount(capsys, monkeypatch):
    """
    Test Case TC-2.1: Credit Account with Valid Amount
    """
    monkeypatch.setattr("builtins.input", lambda _: "200.00")
    operations("CREDIT")
    captured = capsys.readouterr()
    assert "Account credited successfully. New Balance: 1200.00" in captured.out
    assert read_balance() == 1200.00

def test_credit_zero_amount(capsys, monkeypatch):
    """
    Test Case TC-2.2: Credit Account with Zero Amount
    """
    monkeypatch.setattr("builtins.input", lambda _: "0.00")
    operations("CREDIT")
    captured = capsys.readouterr()
    assert "Account credited successfully. New Balance: 1000.00" in captured.out
    assert read_balance() == 1000.00

def test_credit_negative_amount(capsys, monkeypatch):
    """
    Test Case TC-2.3: Credit Account with Negative Amount
    """
    monkeypatch.setattr("builtins.input", lambda _: "-100.00")
    operations("CREDIT")
    captured = capsys.readouterr()
    assert "Account credited successfully. New Balance: 1100.00" in captured.out
    assert read_balance() == 1100.00

def test_credit_invalid_amount(capsys, monkeypatch):
    """
    Test Case TC-2.4: Credit Account with Invalid Amount
    """
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    operations("CREDIT")
    captured = capsys.readouterr()
    assert "Account credited successfully. New Balance: 1000.00" in captured.out
    assert read_balance() == 1000.00

def test_debit_valid_amount(capsys, monkeypatch):
    """
    Test Case TC-3.1: Debit Account with Valid Amount
    """
    monkeypatch.setattr("builtins.input", lambda _: "300.00")
    operations("DEBIT")
    captured = capsys.readouterr()
    assert "Account debited successfully. New Balance: 700.00" in captured.out
    assert read_balance() == 700.00

def test_debit_negative_amount(capsys, monkeypatch):
    """
    Test Case TC-3.2: Debit Account with Negative Amount
    """
    monkeypatch.setattr("builtins.input", lambda _: "-300.00")
    operations("DEBIT")
    captured = capsys.readouterr()
    assert "Account debited successfully. New Balance: 700.00" in captured.out
    assert read_balance() == 700.00

def test_debit_amount_greater_than_balance(capsys, monkeypatch):
    """
    Test Case TC-3.3: Debit Account with Amount Greater Than Balance
    """
    monkeypatch.setattr("builtins.input", lambda _: "2000.00")
    operations("DEBIT")
    captured = capsys.readouterr()
    assert "Insufficient funds. Debit amount exceeds current balance." in captured.out
    assert read_balance() == 1000.00

def test_debit_zero_amount(capsys, monkeypatch):
    """
    Test Case TC-3.4: Debit Account with Zero Amount
    """
    monkeypatch.setattr("builtins.input", lambda _: "0.00")
    operations("DEBIT")
    captured = capsys.readouterr()
    assert "Account debited successfully. New Balance: 1000.00" in captured.out
    assert read_balance() == 1000.00

def test_debit_invalid_amount(capsys, monkeypatch):
    """
    Test Case TC-3.5: Debit Account with Invalid Amount
    """
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    operations("DEBIT")
    captured = capsys.readouterr()
    assert "Account debited successfully. New Balance: 1000.00" in captured.out
    assert read_balance() == 1000.00

def test_invalid_operation_type(capsys):
    """
    Test Case TC-4.1: Invalid Operation Type
    """
    operations("INVALID")
    captured = capsys.readouterr()
    assert "Invalid operation type." in captured.out
