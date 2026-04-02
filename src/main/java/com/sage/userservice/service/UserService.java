package com.sage.userservice.service;

import org.springframework.stereotype.Service;

@Service
public class UserService {
    // Add the new HelloController to the list of controllers in this service
    private final HelloController helloController;

    public UserService(HelloController helloController) {
        this.helloController = helloController;
    }
}
