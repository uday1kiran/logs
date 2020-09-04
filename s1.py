#part of code
def getSubscription():
    subscription_client = get_client_from_cli_profile(SubscriptionClient)
    subscription = next(subscription_client.subscriptions.list())
    print(subscription.subscription_id)

def switchSubscription(subscription_arg):
    # Get subs client
    subscription_client = get_client_from_cli_profile(SubscriptionClient)
    print(subscription_client.subscriptions.list())
    subscription = next(subscription_client.subscriptions.list())
    print(subscription.subscription_id)
    if subscription_arg != subscription.subscription_id:
        print(os.system("az account set --subscription "+subscription_arg))
        lock_client = get_client_from_cli_profile(ManagementLockClient)
        compute_client=get_client_from_cli_profile(ComputeManagementClient)
        resource_client = get_client_from_cli_profile(ResourceManagementClient)
    getSubscription()