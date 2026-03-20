package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class HelloWorldTest {

    @Test
    void greetWorld() {
        assertEquals("Hello, World!", HelloWorld.greet("World"));
    }

    @Test
    void greetCustomName() {
        assertEquals("Hello, Java!", HelloWorld.greet("Java"));
    }

    @Test
    void greetNullFallsBackToWorld() {
        assertEquals("Hello, World!", HelloWorld.greet(null));
    }

    @Test
    void greetBlankFallsBackToWorld() {
        assertEquals("Hello, World!", HelloWorld.greet("  "));
    }
}
