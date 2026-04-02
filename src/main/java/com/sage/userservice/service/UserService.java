package com.sage.userservice.service;

import org.springframework.stereotype.Service;

@Service
public class UserService {
    // ... existing code ...

    public String getVersion() {
        return "1.0.0";
    }
}
