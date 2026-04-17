package com.sage.userservice.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class VersionController {
    private final UserService userService;

    public VersionController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/version")
    public String getVersion() {
        return userService.getVersion();
    }
}
