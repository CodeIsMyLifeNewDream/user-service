package com.sage.userservice.service;

import com.sage.userservice.model.Address;
import com.sage.userservice.repository.AddressRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AddressService {

    private final AddressRepository addressRepository;

    public AddressService(AddressRepository addressRepository) {
        this.addressRepository = addressRepository;
    }

    public List<Address> getAllAddresses() {
        return addressRepository.findAll();
    }

    public Address getAddressById(Long id) {
        return addressRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Address not found with id: " + id));
    }

    public Address createAddress(Address address) {
        return addressRepository.save(address);
    }

    public Address updateAddress(Long id, Address addressDetails) {
        Address address = getAddressById(id);
        address.setStreet(addressDetails.getStreet());
        address.setCity(addressDetails.getCity());
        address.setState(addressDetails.getState());
        address.setZipCode(addressDetails.getZipCode());
        address.setCountry(addressDetails.getCountry());
        return addressRepository.save(address);
    }

    public void deleteAddress(Long id) {
        Address address = getAddressById(id);
        addressRepository.delete(address);
    }
}
