package ezocalc.structure;

import java.math.BigDecimal;

public class Value implements Bloc{

	BigDecimal value;

	public Value(String value) throws SyntaxError {
		try {
			this.value = BigDecimal.valueOf(Double.valueOf(value));
		} catch (Exception e) {
			throw new SyntaxError("Invalid value : " + value);
		}
	}

	public Value(BigDecimal value) throws SyntaxError {
		this.value = value;
	}

	public BigDecimal getValue() {
		return value;
	}

	public boolean is_operand() {
		return false;
	}

}
