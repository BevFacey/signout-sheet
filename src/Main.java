package src;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;


public class Main {
    public static void main(String[] args) {
        System.out.println("starting signout program");
        try (Stream<String> lines = Files.lines(Paths.get("students.csv"))) {
            lines.forEach(System.out::println);
        } catch (IOException e) {
            System.out.println("Error reading file students.csv");
        }
    }
}
