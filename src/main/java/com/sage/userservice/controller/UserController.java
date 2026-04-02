package com.sage.userservice.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1")
public class UserController {

    // New method to return hardcoded version number
    @GetMapping("/version")
    public String getVersion() {
        return "1.0.0";
    }
}
