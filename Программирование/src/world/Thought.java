package world;

public enum Thought {
    BEGINNING("Затевая разводить коз"),
    NOT_THINKING(" я не думал о молоке"),
    REALIZATION("мне пришло в голову, что я могу их доить и получать молоко");

    private final String message;

    Thought(String message) {
        this.message = message;
    }

    public String getMessage() {
        return message;
    }
}
