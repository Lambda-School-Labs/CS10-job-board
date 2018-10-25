import React from 'react';
import axios from 'axios';
import { Alert, Form, Input, InputNumber } from 'antd';
import { CardElement, injectStripe } from 'react-stripe-elements';

const FormItem = Form.Item;

class CheckoutForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      pay: false,
      error: null,
      message: null,
      quantity: null,
      total: null
    }
  }

  showStripeCheckout = () => {
    this.setState({ pay: true });
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  }

  updateQuantity = e => {
    this.setState({ quantity: e, total: e * this.props.price });
  }

  handlePayment = e => {
    e.preventDefault();
    this.setState({ error: null, message: null });
    const { cardholder_name } = this.state;
    // Tokenize purchase with stripe object from injectStripe component
    this.props.stripe.createToken({ name: `${cardholder_name}` })
      .then(response => {
        // console.log(response);
        const stripe_token = response.token.id;
        const token = localStorage.getItem('token');
        // console.log(stripe_token, typeof(stripe_token));
        // compare token to token set in App.js when user logged in.
        if (token !== this.props.token) {
          this.props.logOut(e, `Error authenticating account. Please log in again.`);
        } else {
          const requestOptions = { headers: { Authorization: `JWT ${token}` }};
          axios.post(`${process.env.REACT_APP_API}pay/`, {
              stripe_token: stripe_token,
              user: this.props.user,
              purchased: this.props.product,
              quantity: this.state.quantity
            }, requestOptions )
            .then(response => {
              this.setState({ message: `Payment successful!`});
            })
            .catch(err => {
              this.setState({ error: `Problem saving your payment. Try again.`});
            });
        }
      })
      .catch(err => {
        this.setState({ error: `Problem processing your payment. Try again.`})
      });
  }

  render() {
    const { error, message, pay, quantity, total } = this.state;
    const { getFieldDecorator } = this.props.form;

    return (
      <div className="checkout-form">
        {error ? (
          <Alert message={error} type="error" closable showIcon banner/>
          ) : (null)}
        {message ? (
          <Alert message={message} type="success" closable showIcon banner/>
        ) : (null)}
          <FormItem label="Cardholder Name">
            {getFieldDecorator('cardholder_name', {
              rules: [{
                required: true,
                message: 'Please add the cardholder name',
              }],
            })(
              <Input placeholder="Full name on the card" name="cardholder_name" onChange={this.onChange}/>
            )}
          </FormItem>

          {/* If product is 1 Job, show Quantity to buy multiple */}
          {this.props.product === `sku_DoNhM1EGgKGLeg` ? (
            <FormItem label="Number of jobs" style={{ width: "90px"}}>
              <InputNumber
                onChange={this.updateQuantity} name="quantity" id="quantity"
                step={1}
                min={1}
                defaultValue={1}
                max={11}
                value={quantity}
              />
            </FormItem>
          ) : (null)}

        <div style={{ margin: "40px 0"}}>
            <CardElement />
        </div>
        <h3>Total: {total ? `$${total}` : `$0`}</h3>
        <button onClick={this.handlePayment}>Buy</button>
      </div>
    );
  }
}

// export default injectStripe(CheckoutForm);
export default CheckoutForm = Form.create()(injectStripe(CheckoutForm));