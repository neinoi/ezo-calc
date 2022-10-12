package ezocalc.structure;

import java.math.BigDecimal;

public interface Bloc {

    // Returns value of the bloc (direct value or calculation)
    BigDecimal getValue() throws SyntaxError;
}
