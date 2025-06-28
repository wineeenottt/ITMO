package Move;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public class DoubleTeam extends StatusMove {
   static  Type TYPE = Type.NORMAL;
   static  double POWER = 0;
   static double ACCURACY = 0;

    public DoubleTeam() {
        super(TYPE, POWER, ACCURACY);
    }
    @Override
    protected String describe() {
        return "Применил Double Team";
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        // Проверяем текущее значение уклончивости
        if (p.getStat(Stat.EVASION) < 6) { // Максимальное значение уклончивости - 6
            p.setMod(Stat.EVASION, +1);
        }
    }
}
