import java.util.Arrays;

public class bug6_fixed {
    public static int highestTemperature(int[] readings) {
        if (readings == null || readings.length == 0) {
            throw new IllegalArgumentException("readings must not be empty");
        }

        // Initialize from an actual reading, not zero.
        int highest = readings[0];
        for (int temperature : readings) {
            if (temperature > highest) {
                highest = temperature;
            }
        }
        return highest;
    }

    public static void main(String[] args) {
        int[] readings = {-7, -2, -5};
        System.out.println("Readings: " + Arrays.toString(readings));
        System.out.println("Highest temperature: " + highestTemperature(readings));
    }
}
