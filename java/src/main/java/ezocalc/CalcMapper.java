package ezocalc;

import java.util.ArrayList;
import java.util.List;

import ezocalc.structure.Bloc;
import ezocalc.structure.Operand;
import ezocalc.structure.Operation;
import ezocalc.structure.SyntaxError;
import ezocalc.structure.Value;

public class CalcMapper {

	private static final char[] OPERATORS = { '*', '/', '+', '-', '^' };

	private Operation operation = new Operation();

	public Operation scan(String expression) throws SyntaxError {
		expression = expression.trim().replace(",", ".").replace(" ", "");

		while (expression.indexOf('(') != -1) {
			// maps first elements
			if (expression.indexOf('(') > 0) {
				mapSimple(expression.substring(0, expression.indexOf('(')));
				expression = expression.substring(expression.indexOf('('));
			}

			// must find corresponding closing
			int pos_end = expression.indexOf(')');
			int count_open = countChar(expression.substring(0, pos_end), '(');
			int count_close = 1;
			while (count_open != count_close) {
				pos_end = expression.indexOf(')', pos_end + 1);
				count_open = countChar(expression.substring(0, pos_end), '(');
				count_close++;
			}

			CalcMapper mapper = new CalcMapper();
			operation.append(mapper.scan(expression.substring(1, pos_end)));

			expression = expression.substring(pos_end + 1);
		}

		// remaining mapping
		if (expression.trim().length() > 0) {
			mapSimple(expression);
		}

		return operation;
	}

	private void mapSimple(String sub) throws SyntaxError {
		List<Bloc> splits = new ArrayList<>();

		String acc = "";

		for (char l : sub.toCharArray()) {
			if (isOperator(l)) {
				boolean addOpe = true;

				if (acc.length() > 0) {
					splits.add(new Value(acc));
					acc = "";
				} else if (splits.size() > 0 && splits.get(splits.size() - 1) instanceof Operand && l != '-') {
					throw new SyntaxError("Too many operands found");
				} else if (((splits.size() > 0 && splits.get(splits.size() - 1) instanceof Operand)
						|| splits.size() == 0) && l == '-') {
					acc += "-";
					addOpe = false;
				}

				if (addOpe) {
					splits.add(new Operand(l));
				}
			} else {
				acc += l;
			}
		}

		if (acc.length() > 0) {
			splits.add(new Value(acc));
		}

		for (Bloc b : splits) {
			operation.append(b);
		}

	}

	private int countChar(String str, char chr) {
		int count = 0;
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == chr) {
				count++;
			}
		}
		return count;
	}

	private boolean isOperator(char c) {
		for (char o : OPERATORS) {
			if (o == c) {
				return true;
			}
		}
		return false;
	}
}
