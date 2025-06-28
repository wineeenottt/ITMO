package Move;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public class ScaryFace extends StatusMove {
    static Type TYPE = Type.NORMAL;
    static double POWER = 0;
    static double ACCURACY = 100;

    public ScaryFace() {
        super(TYPE, POWER, ACCURACY);
    }

    @Override
    protected String describe() {
        return " Применил Scary Face";
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        // Снижение скорости цели на 2 этапа
        p.setMod(Stat.SPEED, -2);
    }
}
