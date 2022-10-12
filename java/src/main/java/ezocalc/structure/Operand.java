package ezocalc.structure;

import java.math.BigDecimal;

public class Operand implements Bloc {


    char opcode;

    public Operand(char c) {
    	this.opcode = c;
    }
  
    public BigDecimal calculate(Bloc left, Bloc right) throws SyntaxError {
        switch (opcode) {
        case '+':
        	return left.getValue().add(right.getValue());
        case '-':
            return left.getValue().subtract(right.getValue());
        case '*':
            return left.getValue().multiply(right.getValue());
        case '/':
        	if (right.getValue().doubleValue() == 0) {
        		throw new SyntaxError("Division by zero");
        	}
            return left.getValue().divide(right.getValue());
        case '^':
        	try {
        		int pow = right.getValue().intValueExact();
        		return left.getValue().pow(pow);
        	} catch (ArithmeticException e) {
        		return BigDecimal.valueOf(Math.pow(left.getValue().doubleValue(), right.getValue().doubleValue()));
        	}
        }
    	return null;
    }

    public boolean isFirst() {
    	return opcode == '^';
    }
        

    public boolean isSecond() {
        return opcode == '*' || opcode == '/';
    }
	
	public BigDecimal getValue() {
		return null;
	}

}
