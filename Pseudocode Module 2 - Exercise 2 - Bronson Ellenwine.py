Start
initialize_variables
account_balance = 0
overdrawn_fee = 0
collect_input
account_balance = get_account_balance
times_overdrawn = get_times_overdrawn
process_data
overdrawn_fee = (account_balance * 0.01) - (5 * times_overdrawn)
new_account_balance = account_balance - overdrawn_fee
display_output
print_fee overdrawn_fee
print_new_account_balance new_account_balance
print_message "Thanks for using this program"
End
