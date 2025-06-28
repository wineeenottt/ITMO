package building.exceptions;

public class CheckedException extends Exception {
    @Override
    public String getMessage() {
        return "!!! Вес продуктов превышает допустимый предел !!!";
    }
}
