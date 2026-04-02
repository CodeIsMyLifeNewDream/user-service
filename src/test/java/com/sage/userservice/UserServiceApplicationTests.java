package com.sage.userservice;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.reactive.server.WebTestClient;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class UserServiceApplicationTests {
    @Autowired
    private WebTestClient webTestClient;

    @Test
    public void contextLoads() {
        // Add the new HelloController to the list of controllers in this test
    }
}
