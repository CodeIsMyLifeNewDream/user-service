### src/main/java/com/sage/userservice/model/User.java
```diff
package com.sage.userservice.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
+ import java.time.LocalDateTime;

@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank
    @Column(nullable = false)
    private String name;

    @NotBlank
    @Email
    @Column(nullable = false, unique = true)
    private String email;
+ 
+   @Column(nullable = false)
+   private String temporaryPassword;
+ 
+   @Column(nullable = false)
+   private LocalDateTime passwordResetExpirationTime;

    public User() {
    }

    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
+ 
+   public String getTemporaryPassword() {
+       return temporaryPassword;
+   }
+ 
+   public void setTemporaryPassword(String temporaryPassword) {
+       this.temporaryPassword = temporaryPassword;
+   }
+ 
+   public LocalDateTime getPasswordResetExpirationTime() {
+       return passwordResetExpirationTime;
+   }
+ 
+   public void setPasswordResetExpirationTime(LocalDateTime passwordResetExpirationTime) {
+       this.passwordResetExpirationTime = passwordResetExpirationTime;
+   }
}
```

### src/main/java/com/sage/userservice/controller/UserController.java
```diff
package com.sage.userservice.controller;

import com.sage.userservice.model.User;
import com.sage.userservice.service.UserService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
+ import java.util.UUID;

@RestController
@RequestMapping("/api/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping
    public ResponseEntity<List<User>> getAllUsers() {
        return ResponseEntity.ok(userService.getAllUsers());
    }

    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        return ResponseEntity.ok(userService.getUserById(id));
    }

    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody User user) {
        return ResponseEntity.status(HttpStatus.CREATED).body(userService.createUser(user));
    }

    @PutMapping("/{id}")
    public ResponseEntity<User> updateUser(@PathVariable Long id, @Valid @RequestBody User user) {
        return ResponseEntity.ok(userService.updateUser(id, user));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
        return ResponseEntity.noContent().build();
    }
+ 
+   @PostMapping("/reset-password")
+   public ResponseEntity<String> resetPassword(@RequestBody ResetPasswordRequest request) {
+       User user = userService.getUserByEmail(request.getEmail());
+       if (user == null) {
+           return ResponseEntity.badRequest().body("No user found with email: " + request.getEmail());
+       }
+ 
+       String temporaryPassword = UUID.randomUUID().toString();
+       LocalDateTime passwordResetExpirationTime = LocalDateTime.now().plusHours(1);
+ 
+       user.setTemporaryPassword(temporaryPassword);
+       user.setPasswordResetExpirationTime(passwordResetExpirationTime);
+ 
+       return ResponseEntity.ok("Password reset email sent to " + request.getEmail());
+   }
}
```

### src/main/java/com/sage/userservice/service/UserService.java
```diff
package com.sage.userservice.service;

import com.sage.userservice.model.User;
import com.sage.userservice.repository.UserRepository;
+ import java.time.LocalDateTime;
+ import java.util.UUID;

public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    public User getUserById(Long id) {
        return userRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("User not found with id: " + id));
    }

    public User createUser(User user) {
        return userRepository.save(user);
    }

    public User updateUser(Long id, User userDetails) {
        User user = getUserById(id);
        user.setName(userDetails.getName());
        user.setEmail(userDetails.getEmail());
        return userRepository.save(user);
    }

    public void deleteUser(Long id) {
        User user = getUserById(id);
        userRepository.delete(user);
    }
+ 
+   public User getUserByEmail(String email) {
+       return userRepository.findByEmail(email);
+   }
}
```

### src/test/java/com/sage/userservice/UserServiceApplicationTests.java
```diff
package com.sage.userservice;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class UserServiceApplicationTests {

    @Test
    void contextLoads() {
    }
}