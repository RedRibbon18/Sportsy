#  Single Bet Placement Test Plan


## 01a - User can place a Bet on an Upcoming Match - Away outcome
- `Priority`: Critical
- `Risk Rationale`: Main Flow/Happy path. One sinlge bet on one upcoming match with funds. If this one doesn't pass, feature can not be approved, since the main functionality wll be broken. 
- `Steps`: 
   1. **Pre-conditions**: valid user logged in, with enough funds.
   2. Search for an UPCOMING match
   3. Click on the "2" button on the match found on step 2, to bet for away win and wait for the `bet slip`
   5. Verify `place bet` button is not clickable wihtouth a stake.
   6. Write a valid stake (between  €1.00 and  €100.00) int he `stake` input field
   7. Verify:
      - `total stake` shown matches the one wrote on the previous step
      -  Available balance is being shown
      - `Potential payout` matches stake * odss
      - `Place bet` button is now clickable
   8. Click `Place Bet` button
- `Expected Result`: Bet is placed successfully:
  - stake is deducted from user funds
  - success receipt modal appears showing correct info for:
    - Bet ID
    - Match details
    - Selection
    - Stake
    - Odds at placement
    - Potential payout
    - Placement timestamp
  - Clicking on `CLOSE` button in the `success receipt modal` returns user to main flow without active selection

## 01b - User can place a Bet on an Upcoming Match - Draw outcome
- `Priority`: Critical
- `Risk Rationale`: Main Flow/Happy path. One sinlge bet on one upcoming match with funds. If this one doesn't pass, feature can not be approved, since the mail functionality wll be broken. 
- `Steps`: 
   1. **Pre-conditions**: valid user logged in, with enough funds.
   2. Search for an UPCOMING match
   3. Click on the `X` button on the match found on step 2, to bet for away win and wait for the `bet slip`
   5. Verify `place bet` button is not clickable wihtouth a stake.
   6. Write a valid stake (between  €1.00 and  €100.00) int he `stake` input field
   7. Verify:
      - `total stake` shown matches the one wrote on the previous step.
      -  Available balance is being shown
      - `Potential payout` matches stake * odss
      - `Place bet` button is now clickable
   8. Click `Place Bet` button
- `Expected Result`: Bet is placed successfully:
  - stake is deducted from user funds
  - success receipt modal appears showing correct info for:
    - Bet ID
    - Match details
    - Selection
    - Stake
    - Odds at placement
    - Potential payout
    - Placement timestamp
  - Clicking on `CLOSE` button in the `success receipt modal` returns user to main flow without active selection


## 01c - User can place a Bet on an Upcoming Match - Home outcome
- `Priority`: Critical
- `Risk Rationale`: Main Flow/Happy path. One sinlge bet on one upcoming match with funds. If this one doesn't pass, feature can not be approved, since the mail functionality wll be broken. 
- `Steps`: 
   1. **Pre-conditions**: valid user logged in, with enough funds.
   2. Search for an UPCOMING match
   3. Click on the `1` button on the match found on step 2, to bet for away win and wait for the `bet slip`
   5. Verify `place bet` button is not clickable wihtouth a stake.
   6. Write a valid stake (between  €1.00 and  €100.00) int he `stake` input field
   7. Verify:
      - `total stake` shown matches the one wrote on the previous step
      -  Available balance is being shown
      - `Potential payout` matches stake * odss
      - `Place bet` button is now clickable
   8. Click `Place Bet` button
- `Expected Result`: Bet is placed successfully:
  - stake is deducted from user funds
  - success receipt modal appears showing correct info for:
    - Bet ID
    - Match details
    - Selection
    - Stake
    - Odds at placement
    - Potential payout
    - Placement timestamp
  - Clicking on `CLOSE` button in the `success receipt modal` returns user to main flow without active selection

## 02 - Bet Slip: User can Select between different outcomes
- `Priority`: High
- `Risk Rationale`: User shuld be able to bet for the outcome he wants, we want all 3 outcomes available for betting so we don't lose transactions. Not critical beacuse system is still functional.
- `Steps`: 
   1. **Pre-conditions**: valid user logged in, with enough funds.
   2. Search for an UPCOMING match: date should be in the future, and an upcoming tag should be present.  
   3. Click on the `2` button on the match found on step 2, to bet for away win and wait for the `bet slip` box to show.
   4. Verify data present on the `bet slip` box matches the shown on the match row:
      - teams names
      - teams names order (home vs away)
      - match winner (in this case "away")
      - odds
   5. Click on the `1` button on the match found on step 2, to bet for home win and wait for the `bet slip` box to be updated.
   6. Click on the `X` button on the match found on step 2, to bet for a draw and wait for the `bet slip` box to be updated.
- `Expected Result`: 
    - Bet slip box information shown is being updated wiht valid data on each outcome selected, replacing previous selection.
    - No extra `bet slip` box is being shown.

## 03 - User can See football matches information properly
- `Priority`: High
- `Risk Rationale`: User should be able to see the proper data, so there's no confusion about what it is that he is betting on to avoid legal issues and commplains. Not critical beacuse system is still functional.
- `Steps`: 
   1. **Pre-conditions**: valid user logged in
   2. Search for an `UPCOMING` match: date should be in the future, and an upcoming tag should be present. 
- `Expected Result`: the following information is bieng shown properly in row:
    - Home team vs away team
    - kickoff date/time label
    - Only `UPCOMING` matches should be shown.
    - League. **NOTE**: this is not part of the functional requirments but it is present in the feature, should be discussed with PM
    - 3 selectable odds buttons: `1`, `X`, `2`, with  correspondant odds written below .

## 04 - User can Not place 2 bets on same match
- `Priority`: Critical
- `Risk Rationale`: By specification this is a single bet feature, this scenario should not be allow to the user, it could cause odd behaviours which could end up as money loss for business or legal issues.
- `Steps`: 
   1. **Pre-conditions**: valid user logged in, with enough funds.
   2. Search for an UPCOMING match
   3. Click on the "2" button on the match found on step 2, to bet for away win and wait for the `bet slip`
   5. Verify `place bet` button is not clickable wihtouth a stake.
   6. Write a valid stake (between  €1.00 and  €100.00) in the `stake` input field
   8. Click `Place Bet` button
   9. Verify bet was placed successfully and close Success modal
   10. Search for the same match
   11. Try to place another bet.
- `Expected Result`: User is not allowed to place 2 bets in the same match. **NOTE**: how this should happen is not specify in the feature but it could be:
    -  Match dissapears from list after first bet
    -  `Place Bet` button remains unclickable after filling `Stake` input
    -  Placing bet fails with correspondent error (bet already in progress)
  

## 05 - User can Not place bets with Not Enough Funds
- `Priority`: Critical
- `Risk Rationale`: if user does not have enough money in funds to match the stake, we should not let him place it. (Money loss)
- `Steps`: 
   1. **Pre-conditions**: valid user logged in, with some funds.
   2. Search for an UPCOMING match
   3. Click on the "2" button on the match found on step 2, to bet for away win and wait for the `bet slip` box to show
   6. In  the `stake` input field, write a valid stake, but for more money than available in user funds.
- `Expected Result`: 
    - `Place Bet` button is not clickable
    - UI message for "Must not exceed available balance" should be shown.

## 06 - User can retry bet after placing bet failure.
- `Priority`: Medium
- `Risk Rationale`: If placing of a bet fails, we want to make sure that the app is still functional and user can retry. Not critical beacuse we shouldn't have  to deal with this scenario pretty often.
- `Steps`: 
   1. **Pre-conditions**: valid user logged in
   2. Search for an `UPCOMING` match: date should be in the future, and an upcoming tag should be present. 
   3. Place any bet and somehow make it fail after clicking "Place Bet" (i.e. make transaction to time out)
- `Expected Result`: An error modal with the following information and options pops up:
    - Modal title: Something went wrong
    - Explanation that the bet could not be processed and suggests trying again.
    - Action buttons present: 
       - Rebet (primary): on click it closes the modal and retries placement.
       - Close (secondary): closes modal and clears current selection/stake.
       - top-right X : same behavior as Close.
    - User can still use the app as usual

## 07 - User can Not place bet for past match
- `Priority`: Critical
- `Risk Rationale`: there's no point in betting for something that laready happened. 
- `Steps`: 
   1. **Pre-conditions**: valid user logged in, with enough funds.
   2. Search for a past match
   3. Click on the "2" button on the match found on step 2, to bet for away win and wait for the `bet slip`
   5. Verify `place bet` button is not clickable wihtouth a stake.
   6. Write a valid stake (between  €1.00 and  €100.00) in the `stake` input field
   8. Click `Place Bet` button
- `Expected Result`: User is not allowed to place a bet for a past match. **NOTE**: how this should happen is not specify in the feature but it could be:
    -   Past matches should not be listed
    -  `Place Bet` button remains unclickable after filling `Stake` input
    -   Placing bet fails with correspondent error (can not bet for past matches)

