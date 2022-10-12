package ezocalc.structure;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class Operation implements Bloc {

	List<Bloc> blocs = new ArrayList<>();

	public void append(Bloc b) {
		blocs.add(b);
	}

	public BigDecimal getValue() throws SyntaxError {
		// Returns value of the bloc (direct value or calculation)

		int pos = findOpe();

		while (pos != -1) {
			Operand ope = (Operand) blocs.get(pos);

			BigDecimal val = ope.calculate(blocs.get(pos - 1), blocs.get(pos + 1));
			blocs.set(pos - 1, new Value(val));
			blocs.remove(pos);
			blocs.remove(pos);

			pos = findOpe();
		}

		return blocs.get(0).getValue();
	}

	private Integer findOpe() {

		for (int i = 0; i < blocs.size(); i++) {
			Bloc b = blocs.get(i);
			if ((b instanceof Operand) && ((Operand) b).isFirst()) {
				return i;
			}
		}

		for (int i = 0; i < blocs.size(); i++) {
			Bloc b = blocs.get(i);
			if (b instanceof Operand && ((Operand) b).isSecond()) {
				return i;
			}
		}

		for (int i = 0; i < blocs.size(); i++) {
			Bloc b = blocs.get(i);
			if (b instanceof Operand) {
				return i;
			}
		}

		return -1;
	}

}
