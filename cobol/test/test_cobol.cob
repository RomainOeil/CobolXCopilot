
	   IDENTIFICATION DIVISION.
	   PROGRAM-ID. TestRunner.

	   DATA DIVISION.
	   WORKING-STORAGE SECTION.
	   01  TEST-CASE-ID        PIC X(6).
	   01  AMOUNT              PIC S9(6)V99.
	   01  FINAL-BALANCE       PIC S9(6)V99 VALUE 1000.00.
	   01  PASSED-OPERATION    PIC X(6).
	   01  ACTUAL-RESULT       PIC X(80).
	   01  EXPECTED-RESULT     PIC X(80).
	   01  STATUS              PIC X(4).

	   PROCEDURE DIVISION.

	   * TC-1.1: View Current Balance
		   MOVE 'TC-1.1' TO TEST-CASE-ID
		   MOVE 'TOTAL ' TO PASSED-OPERATION
		   CALL 'Operations' USING PASSED-OPERATION
		   DISPLAY "Test Case: " TEST-CASE-ID " - View Current Balance"
		   DISPLAY "Expected: The application should display the current balance."
		   DISPLAY "----------------------------------------"

	   * TC-2.1: Credit Account with Valid Amount
		   MOVE 'TC-2.1' TO TEST-CASE-ID
		   MOVE 'CREDIT' TO PASSED-OPERATION
		   MOVE 100.00 TO AMOUNT
		   CALL 'Operations' USING PASSED-OPERATION
		   DISPLAY "Test Case: " TEST-CASE-ID " - Credit Account with Valid Amount"
		   DISPLAY "Expected: The application should display the new balance after adding the credit amount."
		   DISPLAY "----------------------------------------"

	   * TC-2.2: Credit Account with Zero Amount
		   MOVE 'TC-2.2' TO TEST-CASE-ID
		   MOVE 'CREDIT' TO PASSED-OPERATION
		   MOVE 0 TO AMOUNT
		   CALL 'Operations' USING PASSED-OPERATION
		   DISPLAY "Test Case: " TEST-CASE-ID " - Credit Account with Zero Amount"
		   DISPLAY "Expected: The application should display the same balance as before."
		   DISPLAY "----------------------------------------"

	   * TC-2.3: Credit Account with Negative Amount
		   MOVE 'TC-2.3' TO TEST-CASE-ID
		   MOVE 'CREDIT' TO PASSED-OPERATION
		   MOVE -100.00 TO AMOUNT
		   CALL 'Operations' USING PASSED-OPERATION
		   DISPLAY "Test Case: " TEST-CASE-ID " - Credit Account with Negative Amount"
		   DISPLAY "Expected: The application should display the new balance after adding the absolute value of the credit amount."
		   DISPLAY "----------------------------------------"

	   * TC-2.4: Credit Account with Invalid Amount
		   MOVE 'TC-2.4' TO TEST-CASE-ID
		   MOVE 'CREDIT' TO PASSED-OPERATION
		   MOVE abc TO AMOUNT
		   DISPLAY "Simulating input: abc (invalid)"
		   CALL 'Operations' USING PASSED-OPERATION
		   DISPLAY "Test Case: " TEST-CASE-ID " - Credit Account with Invalid Amount"
		   DISPLAY "Expected: The application should display the same balance as before."
		   DISPLAY "----------------------------------------"

	   * TC-3.1: Debit Account with Valid Amount
		   MOVE 'TC-3.1' TO TEST-CASE-ID
		   MOVE 'DEBIT ' TO PASSED-OPERATION
		   MOVE 50.00 TO AMOUNT
		   CALL 'Operations' USING PASSED-OPERATION
		   DISPLAY "Test Case: " TEST-CASE-ID " - Debit Account with Valid Amount"
		   DISPLAY "Expected: The application should display the new balance after subtracting the debit amount."
		   DISPLAY "----------------------------------------"

	   * TC-3.2: Debit Account with Negative Amount
		   MOVE 'TC-3.2' TO TEST-CASE-ID
		   MOVE 'DEBIT ' TO PASSED-OPERATION
		   MOVE -50.00 TO AMOUNT
		   CALL 'Operations' USING PASSED-OPERATION
		   DISPLAY "Test Case: " TEST-CASE-ID " - Debit Account with Negative Amount"
		   DISPLAY "Expected: The application should display the new balance after subtracting the absolute value of the debit amount."
		   DISPLAY "----------------------------------------"

	   * TC-3.3: Debit Account with Amount Greater Than Balance
		   MOVE 'TC-3.3' TO TEST-CASE-ID
		   MOVE 'DEBIT ' TO PASSED-OPERATION
		   MOVE 2000.00 TO AMOUNT
		   CALL 'Operations' USING PASSED-OPERATION
		   DISPLAY "Test Case: " TEST-CASE-ID " - Debit Account with Amount Greater Than Balance"
		   DISPLAY "Expected: The application should display an 'Insufficient funds' message and the balance should remain unchanged."
		   DISPLAY "----------------------------------------"

	   * TC-3.4: Debit Account with Zero Amount
		   MOVE 'TC-3.4' TO TEST-CASE-ID
		   MOVE 'DEBIT ' TO PASSED-OPERATION
		   MOVE 0 TO AMOUNT
		   CALL 'Operations' USING PASSED-OPERATION
		   DISPLAY "Test Case: " TEST-CASE-ID " - Debit Account with Zero Amount"
		   DISPLAY "Expected: The application should display the same balance as before."
		   DISPLAY "----------------------------------------"

	   * TC-3.5: Debit Account with Invalid Amount
		   MOVE 'TC-3.5' TO TEST-CASE-ID
		   MOVE 'DEBIT ' TO PASSED-OPERATION
		   MOVE 0 TO AMOUNT
		   DISPLAY "Simulating input: abc (invalid)"
		   CALL 'Operations' USING PASSED-OPERATION
		   DISPLAY "Test Case: " TEST-CASE-ID " - Debit Account with Invalid Amount"
		   DISPLAY "Expected: The application should display the same balance as before."
		   DISPLAY "----------------------------------------"

	   * TC-4.1: Exit the Application
		   MOVE 'TC-4.1' TO TEST-CASE-ID
		   DISPLAY "Test Case: " TEST-CASE-ID " - Exit the Application"
		   DISPLAY "Expected: The application should display an exit message and terminate."
		   DISPLAY "----------------------------------------"

		   STOP RUN.
