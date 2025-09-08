package Move;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.Type;

public class AncientPower extends SpecialMove {
    static Type TYPE = Type.ROCK;
    static double POWER = 60;
    static double ACCURACY = 0;

    public AncientPower() {
        super(TYPE, POWER, ACCURACY);
    }

    @Override
    protected String describe() {
        return "Применил Ancient Power";
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        // Проверяем шанс
        if (Math.random() < 0.1)
            // Повышаем всю статистику пользователя
            p.setMod(Stat.ATTACK, 1);
        p.setMod(Stat.DEFENSE, 1);
        p.setMod(Stat.SPECIAL_ATTACK, 1);
        p.setMod(Stat.SPECIAL_DEFENSE, 1);
        p.setMod(Stat.SPEED, 1);
    }
}
