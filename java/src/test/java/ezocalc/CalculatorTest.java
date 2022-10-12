package ezocalc;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

import java.math.BigDecimal;

import org.junit.jupiter.api.Test;

import ezocalc.structure.Operation;
import ezocalc.structure.SyntaxError;

class CalculatorTest {

	@Test
	void test_01() throws SyntaxError {
		testCalc("1 + 1", 2);
	}

	@Test
	void test_02() throws SyntaxError {
		testCalc("1 + 2", 3);
	}

	@Test
	void test_03() throws SyntaxError {
		testCalc("1 + -1", 0);
	}

	@Test
	void test_04() throws SyntaxError {
		testCalc("-1 - -1", 0);
	}

	@Test
	void test_05() throws SyntaxError {
		testCalc("5 - 4", 1);
	}

	@Test
	void test_06() throws SyntaxError {
		testCalc("5 * 2", 10);
	}

	@Test
	void test_07() throws SyntaxError {
		testCalc("(2 + 5) * 3", 21);
	}

	@Test
	void test_08() throws SyntaxError {
		testCalc("10 / 2", 5);
	}

	@Test
	void test_09() throws SyntaxError {
		testCalc("2 + 2 * 5 + 5", 17);
	}

	@Test
	void test_10() throws SyntaxError {
		testCalc("2.8 * 3 - 1", BigDecimal.valueOf(7.4));
	}

	@Test
	void test_11() throws SyntaxError {
		testCalc("2^8", 256);
	}

	@Test
	void test_12() throws SyntaxError {
		testCalc("2^8 * 5 - 1", 1279);
	}

	@Test
	void test_13() throws SyntaxError {
		testCalc("4 ^ (1 / 2)", 2);
	}

	@Test
	void test_14() {
		// must fail

		try {
			testCalc("1 / 0", 0);
			fail();
		} catch (SyntaxError e) {
		}
	}

	@Test
	void test_Complex() throws SyntaxError {
		testCalc("(9^(1/2)+3)*5.4", BigDecimal.valueOf(32.4));
	}

	private void testCalc(String formula, Integer attendu) throws SyntaxError {
		testCalc(formula, BigDecimal.valueOf(attendu));
	}

	private void testCalc(String formula, BigDecimal attendu) throws SyntaxError {
		System.out.println("CALCUL : " + formula);
		CalcMapper calcmap = new CalcMapper();

		Operation calcTree;

		calcTree = calcmap.scan(formula);
		assertEquals(attendu.doubleValue(), calcTree.getValue().doubleValue());
	}

}
