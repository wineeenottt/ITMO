package Move;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public class WorkUp extends StatusMove {
    private static final Type TYPE = Type.NORMAL;
    private static final double POWER = 0;
    private static final double ACCURACY = 0;

    public WorkUp() {
        super(TYPE, POWER, ACCURACY);
    }

    @Override
    protected String describe() {
        return "Применил Work Up";
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        // Повышаем атаку на 1 стадию
        p.setMod(Stat.ATTACK, +1);
        // Повышаем специальную атаку на 1 стадию
        p.setMod(Stat.SPECIAL_ATTACK, +1);
    }
}
