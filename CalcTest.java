import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


public class CalcTest {

    @Test
    void testAdd() {
        BasicCalc calc = new BasicCalc();
        assertEquals(5, calc.add(2, 3));
        assertEquals(0, calc.add(-2, 2));
        assertEquals(-5, calc.add(-2, -3));
    }

