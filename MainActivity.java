package com.example.smart_waste_management;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    // Method to open the FAQs activity when the "Open FAQs" button is clicked
    public void openFAQsActivity(View view) {
        Intent intent = new Intent(this, FAQsActivity.class);
        startActivity(intent);
    }

    // Add other methods for handling other button clicks or UI interactions

}

