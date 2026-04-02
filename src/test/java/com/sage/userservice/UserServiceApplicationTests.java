package com.sage.userservice;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.reactive.server.WebTestClient;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class UserServiceApplicationTests {
    @Autowired
    private WebTestClient webTestClient;
    
    // ... existing code ...
    
    @Test
    public void testGetVersion() {
        String version = webTestClient.get().uri("/api/version").exchange().expectStatus().isOk().returnResult(String.class).getResponseBody();
        assertEquals("1.0.0", version);
    }
}
