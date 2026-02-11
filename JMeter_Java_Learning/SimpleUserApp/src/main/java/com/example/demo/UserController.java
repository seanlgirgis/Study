package com.example.demo;

import org.springframework.web.bind.annotation.*;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;

@RestController
@RequestMapping("/api/users")
public class UserController {

    // Simulating a database with concurrent-safe map
    private final Map<Long, String> userDatabase = new ConcurrentHashMap<>();
    private final AtomicLong idGenerator = new AtomicLong();

    @GetMapping
    public List<String> getAllUsers() throws InterruptedException {
        // Simulate database read latency (e.g., 50ms)
        Thread.sleep(50);
        return new ArrayList<>(userDatabase.values());
    }

    @PostMapping
    public String createUser(@RequestBody String name) throws InterruptedException {
        // Simulate heavier processing (e.g., validation, write - 100ms)
        Thread.sleep(100);
        long id = idGenerator.incrementAndGet();
        userDatabase.put(id, name);
        return "User created with ID: " + id;
    }

    @GetMapping("/{id}")
    public String getUser(@PathVariable Long id) {
        return userDatabase.getOrDefault(id, "User not found");
    }
}
