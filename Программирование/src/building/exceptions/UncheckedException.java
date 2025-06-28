package building.exceptions;

public class UncheckedException extends RuntimeException {
    @Override
    public String getMessage() {
        return "!!! Список продуктов пуст !!!";
    }
}
